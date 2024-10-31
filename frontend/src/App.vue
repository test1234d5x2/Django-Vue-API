<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded p-2 mb-3">
            Project Assigner
        </div>

        <button class="bg-transparent border border-white mb-3" data-bs-toggle="modal" data-bs-target="#exampleModal">Add {{ displayed_model }}</button>

        <Tabs 
            :displayed_model="displayed_model"
            :models_list="models_list"
            :changeTab="changeTab"
        />

        <InfoTable
            :headings="headings"
            :data="data_list[displayed_model]"
            :deleteData="deleteData"
        />

        <Modal
            :title="'Add New ' + displayed_model"
            :displayed_model="displayed_model"
            :employeesList="data_list['Employee']"
            :projectsList="data_list['Project']"
            :createData="createData"
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

            async createData(form_data, valid) {
                if (valid) {
                    const response = await fetch(`${BASE_URL}/${this.displayed_model.toLowerCase()}sAPI`, {
                        method: "POST",
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(form_data)
                    })
                    const data = await response.json()

                    console.log(data)

                    if (Object.keys(data['data']).length === 0) {
                        window.alert("An error occurred submitting the data")
                        return
                    }

                    this.data_list[this.displayed_model].push(data['data'])
                    console.log(this.data_list[this.displayed_model])

                }
                else {
                    console.log("Failed Attempt To Add Data To " + this.displayed_model)
                }
            },

            updateHeadings() {
                if (this.data_list[this.displayed_model].length > 0) {
                    this.headings = Object.keys(this.data_list[this.displayed_model][0])
                }
            }
        }

    }
</script>


/** Adding Data
 * await fetch(`${BASE_URL}/employeesAPI`, {
    method: "POST",
    body: JSON.stringify({
        "name": "name",
        "surname": "surname",
        "background": "a description",
        "is_working": true
    })
})
 */



/** Updating Data
 * await fetch(`${BASE_URL}/employeeAPI/{employee_id}`, {
    method: "PUT",,
    body: JSON.stringify({
        "name": "name",
        "surname": "surname",
        "background": "a description",
        "is_working": true
    })
})
 */