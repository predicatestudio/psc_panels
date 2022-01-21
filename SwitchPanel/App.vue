<template>
    <div class="container">
        <SwitchPanel :title=panelData.head :switches=panelData.switches></SwitchPanel>
    </div>
</template>

<script>
import SwitchPanel from './SwitchPanel.vue'
export default {
    name: 'App',
    components: {
        SwitchPanel
    },
    props: {
        panelData: {
            type: Object,
            default: {"switches": [{"label": "Gray Switch"}, {"label": "Blue Switch", "color": "primary"}], "head": "Default Header"}}
    }
}
</script>