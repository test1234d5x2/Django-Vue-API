<template>

    <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" v-model="form_data.name" class="form-control" id="name" placeholder="Alice">
    </div>
    <div class="mb-3">
        <label for="surname" class="form-label">Surname</label>
        <input type="text" v-model="form_data.surname" class="form-control" id="surname" placeholder="Johnson">
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
        <button type="button" class="btn btn-primary" @click="() => createData(form_data, validateForm())">Save changes</button>
    </div>

</template>

<script>

    export default {

        props: {
            createData: {
                type: Function,
                required: true
            }
        },

        data() {
            return {
                form_data: {
                    name: "",
                    surname: "",
                    background: "",
                    is_working: false,
                }
            }
        },

        methods: {
            validateForm() {
                if (!this.form_data.name || this.form_data.name.trim().length === 0) {
                    window.alert("Name cannot be empty.")
                    return false
                }
                else if (this.form_data.length > 30) {
                    window.alert("Name must not be more than 30 characters.")
                    return false
                }


                if (!this.form_data.surname || this.form_data.surname.trim().length === 0) {
                    window.alert("Surname cannot be empty.")
                    return false
                } else if (this.form_data.surname.length > 30) {
                    window.alert("Surname must be 30 characters or less.")
                    return false
                }

                if (!this.form_data.background || this.form_data.background.trim().length === 0) {
                    window.alert("Background cannot be empty.")
                    return false
                }

                if (this.form_data.is_working !== true && this.form_data.is_working !== false) {
                    window.alert("Is Working must be a checked or unchecked.")
                    return false
                }

                return true

            }
        }
    }

</script>