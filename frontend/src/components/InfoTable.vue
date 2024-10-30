<template>

    <table class="table">
        <thead>
            <tr>
                <template v-for="heading in headings">
                    <th v-if="heading != 'id'">
                        <span>{{ format_field_to_text_display(heading) }}</span>
                    </th>
                </template>
                <th>Edit</th>
                <th>Delete</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="record in data">
                <template v-for="(value, key) in record">
                    <td v-if="value === true">Yes</td>
                    <td v-else-if="value === false">No</td>
                    <td v-else-if="key != 'id'">{{ value }}</td>
                </template>
                <td><i class="bi bi-pencil-fill icons"></i></td>
                <td><i class="bi bi-trash icons" @click="() => deleteData(record['id'])"></i></td>
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
            },
            deleteData: {
                type: Function,
                required: true
            }
        },

        methods: {
            format_field_to_text_display(field_name) {
                field_name = String(field_name).replace("_", " ")
                return String(field_name)[0].toUpperCase(0) + String(field_name).slice(1)
            }
        }
    }

</script>

<style>

    .icons {
        cursor: pointer;
    }

</style>