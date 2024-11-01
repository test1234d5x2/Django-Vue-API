<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded p-2 mb-3">
            Project Assigner
        </div>

        <button class="bg-transparent border border-white mb-3" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="() => [setMode('add')]">Add {{ displayed_model }}</button>

        <!--  -->

        <Tabs
            :displayed_model="displayed_model"
            :models_list="models_list"
            :changeTab="changeTab"
        />

        <InfoTable
            :headings="headings"
            :data="data_list[displayed_model]"
            :deleteData="deleteData"
            :setMode="setMode"
            :setEditableData="setEditableData"

        />

        <Modal
            :title="displayed_model"
            :displayed_model="displayed_model"
            :employeesList="data_list['Employee']"
            :projectsList="data_list['Project']"
            :saveChanges="saveChanges"
            :mode="mode"
            :editable_data="editable_data"
            :key="Math.random()"
        />

    </div>
</template>
  
<script>

    import InfoTable from './components/InfoTable.vue';
    import Modal from './components/Modal.vue';
    import Tabs from './components/Tabs.vue';

    const BASE_URL = "http://localhost:8000/api" 

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
                editable_data: {},
                mode: "",
            }
        },

        async mounted() {
            const response = await fetch(`${BASE_URL}/getModels`)
            const data = await response.json()
            this.models_list = data['data']
            this.displayed_model = this.models_list[0]

            for (const model of this.models_list) {                
                var response2 = await fetch(`${BASE_URL}/${model.toLowerCase()}sAPI`)
                var data2 = await response2.json()
                this.data_list[model] = data2['data']
            }

            this.updateHeadings()
        },

        methods: {
            changeTab(name) {
                this.displayed_model = name
                this.updateHeadings()
            },

            setEditableData(record) {
                this.editable_data = record
            },

            setMode(mode) {
                this.mode = mode
                if (mode == "add") {
                    this.editable_data = {}
                }
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
            },

            async saveChanges(form_data, valid, id=NaN) {
                // Add Data
                if (valid && isNaN(id)) {
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
                }

                // Update Data
                else if (valid && id instanceof Number) {
                    const response = await fetch(`${BASE_URL}/${this.displayed_model.toLowerCase()}API/${id}`, {
                        method: "PUT",
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(form_data)
                    })
                }

                else {
                    console.log("Failed Attempt To Add Data To " + this.displayed_model)
                }
            },

            updateHeadings() {
                if (this.data_list[this.displayed_model].length > 0) {
                    this.headings = Object.keys(this.data_list[this.displayed_model][0])
                }
                else {
                    this.headings = []
                }
            }
        }

    }
</script>