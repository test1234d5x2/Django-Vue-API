<template>

    <div class="mb-3">
        <label for="employee" class="form-label">Employee</label>
        <input type="text" v-model="form_data.employee" class="form-control" id="employee">
    </div>
    <div class="mb-3">
        <label for="project" class="form-label">Project</label>
        <input type="text" v-model="form_data.project" class="form-control" id="project">
    </div>
    <div class="mb-3">
        <label for="role" class="form-label">Role</label>
        <input type="text" v-model="form_data.role" class="form-control" id="role" />
    </div>
    <div class="mb-3">
        <label class="form-label" for="weekly_hours">Weekly Hours</label>
        <input type="number" v-model="form_data.weekly_hours" class="form-control" id="weekly_hours" />
    </div>

</template>

<script>

    export default {
        data() {
            return {
                form_data: {
                    employee: "",
                    project: "",
                    role: "",
                    weekly_hours: "",

                }
            }
        }
    }

</script>