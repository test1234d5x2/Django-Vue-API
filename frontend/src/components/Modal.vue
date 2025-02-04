<template>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">{{ title }}</h1>
                <button type="button" class="btn-close" aria-label="Close" data-bs-dismiss="modal" ></button>
            </div>
            <div class="modal-body">
                <template v-if="String(displayed_model).toLowerCase() === 'employee'">
                    <EmployeeForm 
                        @save-changes="(form_data, valid, id) => $emit('save-changes', form_data, valid, id)"
                        :form_data="form_data"
                    />
                </template>
                <template v-else-if="String(displayed_model).toLowerCase() === 'project'">
                    <ProjectForm 
                        @save-changes="(form_data, valid, id) => $emit('save-changes', form_data, valid, id)"
                        :form_data="form_data"
                    />
                </template>
                <template v-else-if="String(displayed_model).toLowerCase() === 'assignment'">
                    <AssignmentForm 
                        :projectsList="projectsList"
                        :employeesList="employeesList"
                        :form_data="form_data"
                        @save-changes="(form_data, valid, id) => $emit('save-changes', form_data, valid, id)"
                    />
                </template>
            </div>
           
            </div>
        </div>
    </div>

</template>

<script>

    import AssignmentForm from './AssignmentForm.vue';
    import EmployeeForm from './EmployeeForm.vue';
    import ProjectForm from './ProjectForm.vue';

    export default {
        components: {
            EmployeeForm,
            ProjectForm,
            AssignmentForm
        },

        props: {
            title: {
                type: String,
                required: true
            },
            displayed_model: {
                type: String,
                required: true
            },
            employeesList: {
                type: Array,
                required: true
            },
            projectsList: {
                type: Array,
                required: true
            },
            mode: {
                type: String,
                required: true
            },
            form_data: {
                type: Object,
                required: true
            },
        }
    }

</script>