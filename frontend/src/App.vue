<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded p-2 mb-3">
            Project Assigner
        </div>

        <button class="bg-transparent border border-white">Add {{ displayed_model }}</button>

        <Tabs 
            :displayed_model="displayed_model"
            :models_list="models_list"
            :changeTab="changeTab"
        />

        <InfoTable
            :headings="headings"
            :data="displayed_data"
            :deleteData="deleteData"
        />

        <!-- Button trigger modal -->
        <!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
        Launch demo modal
        </button> -->

        <!-- Modal -->
        <!-- <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                ...
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
            </div>
            </div>
        </div>
        </div> -->

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
                displayed_data: [],
                headings: []
            }
        },

        async mounted() {
            const response = await fetch(`${BASE_URL}/getModels`)
            const data = await response.json()
            this.models_list = data['data']
            this.displayed_model = this.models_list[0]

            const response2 = await fetch(`${BASE_URL}/${this.displayed_model.toLowerCase()}sAPI`)
            const data2 = await response2.json()
            this.displayed_data = data2['data']

            if (this.displayed_data.length > 0) {
                this.headings = Object.keys(this.displayed_data[0])
            }
        },

        methods: {
            async changeTab(name) {
                this.displayed_model = name
                this.updateDisplayedData()

                if (this.displayed_data.length > 0) {
                    this.headings = Object.keys(this.displayed_data[0])
                }
            },

            async deleteData(id) {
                if (confirm("Are you sure you want to delete this record?")) {
                    const response = await fetch(`${BASE_URL}/${this.displayed_model.toLowerCase()}API/${id}`, {
                        method: "DELETE"
                    })
                    this.updateDisplayedData()
                }
            },

            async updateDisplayedData() {
                const response = await fetch(`${BASE_URL}/${this.displayed_model.toLowerCase()}sAPI`)
                const data = await response.json()
                this.displayed_data = data['data']
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