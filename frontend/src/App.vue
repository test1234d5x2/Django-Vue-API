<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            Project Assigner
        </div>

        <ul class="nav nav-tabs">

            <li class="nav-item" v-for="(model, index) in models_list['data']">
                <a class="nav-link" aria-current="page" href="#" v-if="index !== 0">{{ String(model).charAt(0).toUpperCase() + String(model).slice(1).toLowerCase() }}</a>
                <a class="nav-link active" aria-current="page" href="#" v-else>{{ String(model).charAt(0).toUpperCase() + String(model).slice(1).toLowerCase() }}</a>
            </li>
        </ul>



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

    const BASE_URL = "http://localhost:8000/api"

    export default {

        data() {
            return {
                models_list: '',
            }
        },
        async mounted() {
            const response = await fetch(`${BASE_URL}/listTypes`)
            this.models_list = await response.json()
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