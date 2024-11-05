<template>

    <div class="mb-3">
        <label for="employee" class="form-label">Employee</label>
        <select class="form-select" aria-label="Select Employee" id="employee" v-model="form_data.employee_id">
            <option v-for="employee in employeesList" :value="employee.id">{{employee.name}} {{employee.surname}}</option>
        </select>
    </div>
    <div class="mb-3">
        <label for="project" class="form-label">Project</label>
        <select class="form-select" aria-label="Select Project" id="project" v-model="form_data.project_id">
            <option v-for="project in projectsList" :value="project.id">{{ project.name }}</option>
        </select>
    </div>
    <div class="mb-3">
        <label for="role" class="form-label">Role</label>
        <input type="text" v-model="form_data.role" class="form-control" id="role" />
    </div>
    <div class="mb-3">
        <label class="form-label" for="weekly_hours">Weekly Hours</label>
        <input type="number" v-model="form_data.weekly_hours" class="form-control" id="weekly_hours" />
    </div>
    
    <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" @click="() => saveChanges(form_data, validateForm(), Object.keys(form_data).indexOf('id') === -1 ? -1: form_data['id'])">Save changes</button>
    </div>

</template>

<script>

    export default {

        props: {
            employeesList: {
                type: Array,
                required: true
            },
            projectsList: {
                type: Array,
                required: true
            },
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
                id: NaN,
            }
        },
        
        methods: {
            validateForm() {
                let employeeIdExists = false;
                for (let i = 0; i < this.employeesList.length; i++) {
                    if (this.employeesList[i].id === parseInt(this.form_data.employee_id)) {
                        employeeIdExists = true;
                        break;
                    }
                }
                if (!employeeIdExists) {
                    window.alert("Could not find the employee.")
                    return false
                }

                let projectIdExists = false;
                for (let i = 0; i < this.projectsList.length; i++) {
                    if (this.projectsList[i].id === parseInt(this.form_data.project_id)) {
                        projectIdExists = true;
                    }
                }
                if (!projectIdExists) {
                    window.alert("Could not find the project.")
                    return false
                }

                if (!this.form_data.role || this.form_data.role.length > 100) {
                    window.alert("Role must not be greater than 100 characters")
                    return false
                }

                if (isNaN(this.form_data.weekly_hours) || this.form_data.weekly_hours < 1 || this.form_data.weekly_hours > 40) {
                    window.alert("Weekly Hours must be between 1 and 40.")
                    return false
                }

                return true
            }
        }
    }

</script>