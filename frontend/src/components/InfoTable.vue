<template>

    <table class="table">
        <thead>
            <tr>
                <template v-for="heading in headings">
                    <th v-if="!(heading == 'id' || heading == 'employee_id' || heading == 'project_id')">
                        <span>{{ format_field_to_text_display(heading) }}</span>
                    </th>
                </template>
                <th v-if="headings.length > 0">Edit</th>
                <th v-if="headings.length > 0">Delete</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="record in data">
                <template v-for="(value, key) in record">
                    <td v-if="!excluded_fields.includes(key)">{{ generateDisplayValue(key, value) }}</td>
                </template>
                <!-- <td><i class="bi bi-pencil-fill icons" @click="() => prepareEditForm(record)"></i></td> -->
                <td><i class="bi bi-pencil-fill icons" @click="$emit('prepare-edit-form', record)"></i></td>
                <td><i class="bi bi-trash icons" @click="$emit('delete-data', record['id'])"></i></td>
            </tr>
        </tbody>
    </table>

</template>

<script>

    export default {
        props: {
            headings: {
                type: Array,
                required: true
            },
            data: {
                type: Array,
                required: true
            }
        },

        data() {
            return {
                excluded_fields: ['id', 'employee_id', 'project_id', 'assignment_id']
            }
        },

        methods: {

            // Format the Object keys to be used as headings for the table
            format_field_to_text_display(field_name) {
                field_name = String(field_name).replace("_", " ")
                return field_name[0].toUpperCase(0) + field_name.slice(1)
            },

            // Format dates for displaying
            formate_date_value_to_display(date_value) {
                const date = new Date(date_value)
                return date.toLocaleDateString()
            },

            // Formats the raw data for display
            generateDisplayValue(key, value) {
                if (value === true) return "Yes"
                else if (value === false) return "No"
                else if (key === "start_date") return this.formate_date_value_to_display(value)
                else if (key !== "id") return value
            }
        }
    }

</script>

<style scoped>

    .icons {
        cursor: pointer;
    }

</style>