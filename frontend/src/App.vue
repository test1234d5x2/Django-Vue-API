<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded p-2 mb-3">
            Project Assigner
        </div>

        <button class="bg-transparent border border-white mb-3" @click="() => prepareAddForm()">Add {{ displayed_model }}</button>

        <Tabs
            :displayed_model="displayed_model"
            :models_list="models_list"
            :changeTab="changeTab"
        />

        <InfoTable
            :headings="headings"
            :data="formatted_display_data"
            :deleteData="deleteData"
            :prepareEditForm="prepareEditForm"

        />

        <Modal
            :title="displayed_model"
            :displayed_model="displayed_model"
            :employeesList="data_list['Employee']"
            :projectsList="data_list['Project']"
            :saveChanges="saveChanges"
            :mode="mode"
            :form_data="form_data"
        />

    </div>
</template>
  
<script>

    import * as bootstrap from 'bootstrap'

    import InfoTable from './components/InfoTable.vue';
    import Modal from './components/Modal.vue';
    import Tabs from './components/Tabs.vue';

    const BASE_URL = "http://localhost:8000/api"

    const MODES = {
        "ADD": "add",
        "EDIT": "edit"
    }

    export default {
        components: {
            Tabs,
            InfoTable,
            Modal,
        },

        data() {
            return {
                models_list: [],
                displayed_model: "",
                data_list: {},
                headings: [],
                form_data: {},
                mode: "",
                modal: "",
                formatted_display_data: [],
            }
        },

        async mounted() {
            const response = await fetch(`${BASE_URL}/getModels`)
            const data = await response.json()
            this.models_list = data['data']

            for (const model of this.models_list) {                
                var response2 = await fetch(`${BASE_URL}/${model.toLowerCase()}sAPI`)
                var data2 = await response2.json()
                this.data_list[model] = data2['data']
            }

            this.changeTab(this.models_list[0])
        },

        methods: {
            changeTab(name) {
                this.displayed_model = name
                this.processDisplayData()
                this.updateHeadings()
            },

            processDisplayData() {
                if (this.displayed_model === "Assignment") {
                    let assignmentsList = JSON.parse(JSON.stringify(this.data_list[this.displayed_model]))
                    this.formatted_display_data = assignmentsList.map((record) => {
                        for (let employee of this.data_list['Employee']) {
                            if (employee['id'] === record['employee_id']) {
                                record['employee'] = employee['name'] + " " + employee['surname']
                            }
                        }

                        for (let project of this.data_list['Project']) {
                            if (project['id'] === record['project_id']) {
                                record['project'] = project['name']
                            }
                        }

                        return record
                    })
                }
                else {
                    this.formatted_display_data = this.data_list[this.displayed_model]
                }   
            },

            setEditableData(record) {
                this.form_data = JSON.parse(JSON.stringify(record))
            },

            prepareAddForm() {
                this.setMode(MODES['ADD'])
                this.setEditableData({})

                this.modal = new bootstrap.Modal(document.getElementById("exampleModal"))
                this.toggleModal()
            },

            prepareEditForm(record) {
                this.setMode(MODES['EDIT'])
                this.setEditableData(record)

                this.modal = new bootstrap.Modal(document.getElementById("exampleModal"))
                this.toggleModal()
            },

            toggleModal() {
                this.modal.toggle()
            },

            setMode(mode) {
                this.mode = mode
            },

            async deleteData(id) {
                if (confirm("Are you sure you want to delete this record?")) {
                    const response = await fetch(`${BASE_URL}/${this.displayed_model.toLowerCase()}API/${id}`, {
                        method: "DELETE"
                    })
                    if (response.ok) {
                        this.data_list[this.displayed_model] = this.data_list[this.displayed_model].filter(element => element.id !== id)
                    }
                }

                this.processDisplayData()
            },

            async addData(form_data) {
                const response = await fetch(`${BASE_URL}/${this.displayed_model.toLowerCase()}sAPI`, {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(form_data)
                })
                const data = await response.json()

                if (Object.keys(data['data']).length === 0) {
                    window.alert("An error occurred submitting the data")
                    return
                }

                this.data_list[this.displayed_model].push(data['data'])
            },

            async updateData(form_data, id) {
                const response = await fetch(`${BASE_URL}/${this.displayed_model.toLowerCase()}API/${id}`, {
                    method: "PUT",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(form_data)
                })

                for (let x = 0; x < this.data_list[this.displayed_model].length; x++) {
                    if (this.data_list[this.displayed_model][x]['id'] == id) {
                        this.data_list[this.displayed_model][x] = form_data
                    }
                }
            },

            async saveChanges(form_data, valid, id=-1) {
                // Add Data
                if (valid && this.mode == MODES['ADD']) {
                    await this.addData(form_data)
                }

                // Update Data
                else if (valid && this.record_exists(id, this.displayed_model) && this.mode == MODES['EDIT']) {
                    await this.updateData(form_data, id)
                }

                else {
                    console.log("Failed Attempt To Save Changes.")
                }

                this.processDisplayData()
            },

            record_exists(id, displayed_model) {
                for (let record of this.data_list[displayed_model]) {
                    if (record['id'] === id) {
                        return true
                    }
                }
                return false
            },

            updateHeadings() {
                if (this.formatted_display_data.length > 0) {
                    this.headings = Object.keys(this.formatted_display_data[0])
                }
                else {
                    this.headings = []
                }
            }
        }

    }
</script>