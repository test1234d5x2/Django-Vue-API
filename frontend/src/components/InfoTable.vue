<template>

    <table class="table">
        <thead>
            <tr>
                <template v-for="heading in headings">
                    <th v-if="heading != 'id'">
                        <span>{{ format_field_to_text_display(heading) }}</span>
                    </th>
                </template>
                
            </tr>
        </thead>
        <tbody>
            <tr v-for="record in data">
                <template v-for="(value, key) in record">
                    <td v-if="key != 'id'">{{ value }}</td>
                </template>
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

        methods: {
            format_field_to_text_display(field_name) {
                field_name = String(field_name).replace("_", " ")
                return String(field_name)[0].toUpperCase(0) + String(field_name).slice(1)
            }
        }
    }

</script>