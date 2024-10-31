<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded p-2 mb-3">
            Project Assigner
        </div>

        <button @click="retrieveFormFields" class="bg-transparent border border-white" data-bs-toggle="modal" data-bs-target="#exampleModal">Add {{ displayed_model }}</button>

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

        <!-- Modal Start -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    {{ form_fields }}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
                </div>
            </div>
        </div>
        <!-- Model End -->

    </div>
</template>
  
<script>

    import InfoTable from './components/InfoTable.vue';
    import Tabs from './components/Tabs.vue';

    const BASE_URL = "http://localhost:8000/api" 

    export default {
        components: {
            Tabs,
            InfoTable
        },

        data() {
            return {
                models_list: [],
                displayed_model: "",
                data_list: {},
                headings: [],
                form_fields: [],
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

            async retrieveFormFields() {
                const response = await fetch(`${BASE_URL}/getFormFields/${this.displayed_model.toLowerCase()}`)
                const data = await response.json()
                this.form_fields = data['data']
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



 /** Deleting Data
  * await fetch(`${BASE_URL}/employeeAPI/{employee_id}`, {
        method: "DELETE",
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