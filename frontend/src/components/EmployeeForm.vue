<template>

    <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" v-model="form_data.name" class="form-control" id="name">
    </div>
    <div class="mb-3">
        <label for="surname" class="form-label">Surname</label>
        <input type="text" v-model="form_data.surname" class="form-control" id="surname">
    </div>
    <div class="mb-3">
        <label for="background" class="form-label">Background</label>
        <textarea v-model="form_data.background" class="form-control" id="background" rows="3"></textarea>
    </div>
    <div class="mb-3">
        <label class="form-label" for="is_working">Is working?</label>
        <input class="form-check-input mx-2" type="checkbox" v-model="form_data.is_working" value="1" id="is_working">
    </div>

    <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" @click="$emit('save-changes', form_data, validateForm(), Object.keys(form_data).indexOf('id') === -1 ? -1: form_data['id'])">Save changes</button>
    </div>

</template>

<script>

    export default {

        props: {
            form_data: {
                type: Object,
                required: true
            }
        },

        methods: {

            // Validates the data entered in the form.
            validateForm() {
                let numberRE = /\d/

                // Validate the employee name.
                if (!this.form_data.name || this.form_data.name.trim().length === 0) {
                    window.alert("Name cannot be empty.")
                    return false
                }
                else if (this.form_data.name.length > 30) {
                    window.alert("Name must not be more than 30 characters.")
                    return false
                }
                else if (numberRE.test(this.form_data.name)) {
                    window.alert("Name cannot have numbers.")
                    return false
                }

                 // Validate the employee surname.
                if (!this.form_data.surname || this.form_data.surname.trim().length === 0) {
                    window.alert("Surname cannot be empty.")
                    return false
                } 
                else if (this.form_data.surname.length > 30) {
                    window.alert("Surname must be 30 characters or less.")
                    return false
                }
                else if (numberRE.test(this.form_data.surname)) {
                    window.alert("Surname cannot have numbers.")
                    return false
                }

                // Validate the employee's background description.
                if (!this.form_data.background || this.form_data.background.trim().length === 0) {
                    window.alert("Background cannot be empty.")
                    return false
                }

                if (this.form_data.is_working !== true) {
                    this.form_data.is_working = false
                }

                return true

            }
        }
    }

</script>