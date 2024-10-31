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

</template>

<script>

    export default {
        data() {
            return {
                form_data: {
                    name: "",
                    surname: "",
                    background: "",
                    is_working: "",
                }
            }
        }
    }

</script>