<template>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">{{ title }}</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <template v-if="String(displayed_model).toLowerCase() === 'employee'">
                    <EmployeeForm />
                </template>
                <template v-else-if="String(displayed_model).toLowerCase() === 'project'">
                    <ProjectForm />
                </template>
                <template v-else-if="String(displayed_model).toLowerCase() === 'assignment'">
                    <AssignmentForm />
                </template>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
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
            }
        }
    }

</script>