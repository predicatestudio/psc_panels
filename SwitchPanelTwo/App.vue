<template>
    <div class="container">
        <SwitchPanel :title=panelData.head :switches=panelData.switches></SwitchPanel>
    </div>
</template>

<script>
import SwitchPanel from './SwitchPanelTwo.vue'
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
    // data() {
    //     return {
    //         panelData: {
    //             "switch": null,
    //             "header": null
    //         }
    //     }
    // },
    // created() {
    //     fetch('./switch-panel.json')
    //         .then(response => response.json()
    //         .then(data => {
    //             this.panelData = data;
    //         }))
    //         .catch((e) => {
    //             console.error(e)
    //         })
    // }
}
</script>