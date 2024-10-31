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

</template>

<script>

    export default {
        data() {
            return {
                form_data: {
                    name: "",
                    description: "",
                    start_date: "",
                }
            }
        }
    }

</script>