odoo.define('retenue_a_source.RetenueSourceWidget', function (require) {
    "use strict";
    
    var Widget = require('web.Widget');

    var RetenueSourceWidget = Widget.extend({
        template: 'RetenueSourceWidget',

        init: function (parent, options) {
            this._super.apply(this, arguments);
            // Initialization logic here
        },

        start: function () {
            // Start logic here
            return this._super();
        },
    });

    return RetenueSourceWidget;
});
    
