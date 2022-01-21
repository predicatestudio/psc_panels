// This component is an example of how to use this component in a .vue file.
// Example.vue is not intended to be used for anything other than showcasing and examples.
<template>
    <div class="container">
        <TemplatePanel :title=panelData.head :switches=panelData.switches></TemplatePanel>
    </div>
</template>

<script>
import TemplatePanel from './Template.vue'
export default {
    name: 'App',
    components: {
        TemplatePanel
    },
    props: {
        panelData: Object,
    }
}
</script>