<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            Project Assigner
        </div>

        <Tabs 
            :displayed_model="displayed_model"
            :models_list="Object.keys(models_structure)"
            :changeTab="changeTab"
        />

        <pre>{{ displayed_data }}</pre>





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

    import Tabs from './components/Tabs.vue';

    const BASE_URL = "http://localhost:8000/api" 

    export default {
        components: {
            Tabs
        },

        data() {
            return {
                models_structure: {},
                displayed_model: "",
                displayed_fields: [],
                displayed_data: []
            }
        },

        async mounted() {
            const response = await fetch(`${BASE_URL}/getModelsStructure`)
            this.models_structure = await response.json()
            this.displayed_model = Object.keys(this.models_structure)[0]
            this.displayed_fields = Object.values(this.models_structure)[0]

            const response2 = await fetch(`${BASE_URL}/${this.displayed_model.toLowerCase()}sAPI`)
            const data = await response2.json()
            this.displayed_data = data['data']
        },

        methods: {
            async changeTab(name) {
                this.displayed_model = name
                this.displayed_fields = this.models_structure[name]

                const response = await fetch(`${BASE_URL}/${this.displayed_model.toLowerCase()}sAPI`)
                const data = await response.json()
                this.displayed_data = data['data']
            },
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