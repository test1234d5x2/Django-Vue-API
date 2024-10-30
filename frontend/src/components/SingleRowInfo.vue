<template>

    <div v-for="(value, key) in info">
        <p v-if="key !== 'id'">{{ convert_field_to_display_text(key) }}: {{ value }}</p>
    </div>

</template>

<script>

    export default {
        props: {
            info: {
                type: Object,
                required: true
            }
        },

        methods: {
            convert_field_to_display_text(field_name) {
                field_name = String(field_name).replace("_", " ")

                return String(field_name).charAt(0).toUpperCase() + String(field_name).slice(1)
            }
        }
    }

</script>