// This component is an example of how to use this component in a .vue file.
// Example.vue is not intended to be used for anything other than showcasing and examples.
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
        panelData: Object,
    }
}
</script>