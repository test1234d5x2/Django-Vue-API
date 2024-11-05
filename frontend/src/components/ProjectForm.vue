<template>

    <div class="mb-3">
        <label for="name" class="form-label">Project Name</label>
        <input type="text" v-model="form_data.name" class="form-control" id="name">
    </div>
    <div class="mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea v-model="form_data.description" class="form-control" id="description" rows="3"></textarea>
    </div>
    <div class="mb-3">
        <label for="start_date" class="form-label">Start date</label>
        <input type="date" v-model="form_data.start_date" id="start_date" />
    </div>

    <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" @click="() => saveChanges(form_data, validateForm(), Object.keys(form_data).indexOf('id') === -1 ? -1: form_data['id'])">Save changes</button>
    </div>

</template>

<script>

    export default {
        props: {
            saveChanges: {
                type: Function,
                required: true
            },
            form_data: {
                type: Object,
                required: true
            }
        },

        data() {
            return {
                id: NaN
            }
        },

        methods: {
            validateForm() {
                if (!this.form_data.name || this.form_data.name.trim().length === 0) {
                    window.alert("The project name field cannot be empty.")
                    return false
                }
                else if (this.form_data.name.length > 100) {
                    window.alert("The project name cannot be more than 100 characters.")
                    return false
                }

                if (!this.form_data.description || this.form_data.description.trim().length === 0) {
                    window.alert("The project description must not be empty.")
                    return false
                }

                if (!this.form_data.start_date) {
                    window.alert("The project start date must be set.")
                    return false
                }

                return true
            }
        }
    }

</script>