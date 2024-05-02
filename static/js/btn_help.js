odoo.define('pointage.BtnHelp', function(require) {

    "use strict"
    $(() => {
        var core = require('web.core');
        var ListView = require('web.ListView');
        var ListController = require("web.ListController");

        var includeDict = {
            renderButtons: function() {
                this._super.apply(this, arguments)
                if (this.modelName === "pointage") {
                    var btn = this.$buttons.find('button.o_documents_pointage');
                    btn.on('click', this.proxy('o_documents_pointage'));
                }
                if (this.modelName === "pointage.line") {
                    var btn = this.$buttons.find('button.o_documents_pointage_line');
                    btn.on('click', this.proxy('o_documents_pointage_line'));
                }
                if (this.modelName === "agence.register.doc.bti") {
                    var btn = this.$buttons.find('button.o_documents_pointage_periode');
                    btn.on('click', this.proxy('o_documents_pointage_periode'));
                }
            },
            o_documents_pointage: function() {
                var self = this;
                $('a').attr('target', function() {
                    return '_blank';
                });
            },
            o_documents_pointage_line: function() {
                var self = this;
                $('a').attr('target', function() {
                    return '_blank';
                });
            },
            o_documents_pointage_periode: function() {
                var self = this;
                $('a').attr('target', function() {
                    return '_blank';
                });
            }
        };
        ListController.include(includeDict);
    });
});