<template>

    <ul class="nav nav-tabs">

        <li class="nav-item" v-for="model in models_list">
            <a @click="$emit('change-tab', model)" class="nav-link" aria-current="page" href="#" v-if="model != displayed_model">{{ model }}</a>
            <a @click="$emit('change-tab', model)" class="nav-link active" aria-current="page" href="#" v-else>{{ model }}</a>

        </li>
    </ul>

</template>

<script>

    export default {

        props: {
            displayed_model: {
                type: String,
                required: true
            },
            models_list: {
                type: Array,
                required: true
            },
        },
    }

</script>