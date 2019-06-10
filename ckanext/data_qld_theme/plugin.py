import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckan.common import config


def get_gtm_code():
    # To get Google Tag Manager Code
    gtm_code = config.get('ckan.google_tag_manager.gtm_container_id', False)
    return str(gtm_code)


class DataQldThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IConfigurable, inherit=True)

    def configure(self, config):
        '''Load config settings for this extension from config file.

        See IConfigurable.

        '''
        # print ('configure')
        # import ckan.lib.fanstatic_resources as fanstatic_resources
        # vendor = getattr(fanstatic_resources, 'vendor')
        # resource = vendor.known_resources.pop('bootstrap/js/bootstrap.js', None)
        # print (vars(resource))
        # print (' ')
        # vendor = getattr(fanstatic_resources, 'data_qld_theme')
        # resource = vendor.known_resources.pop('bootstrap/js/bootstrap.js', None)
        # print (vars(resource))

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'data_qld_theme')

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'get_gtm_container_id': get_gtm_code
        }
