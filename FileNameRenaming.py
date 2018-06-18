import os

version = "15.3.0"

directories = [
    'C:/SW/workspace_Luna/jvazquez_integration_repository/XXXX/src/main/resources/assets/js/modules/',
    'C:/SW/workspace_Luna/jvazquez_integration_repository/XXXX/src/main/resources/assets/css/',
    'C:/SW/workspace_Luna/jvazquez_integration_repository/XXXX/src/main/resources/assets/js/'
]

files_to_update = [
    'jquery-migrate-1.2.1.min.js',
    'jquery.jqtransform.js',
    'jquery-ui-1.10.2.custom.js',
    'jquery.placeholder.min.js',
    'jquery.lazyload.min.js',
    'jquery-easing.js',
    'jquery.tinyscrollbar.js',
    'jquery.tools.min.js',
    'jquery.expander.js',
    'jquery.highlight-3.js',
    'jquery.tinycarousel.js',
    'jquery.autocomplete.js',
    'jquery.zclip.min.js',
    'jquery.form.js',
    'jquery.ba-postmessage.js',
    'forrester-core.js',
    'overlay.js',
    'validation.js',
    'hoverContent.js',
    'modernizr.js',
    'main.js',
    'forrester-carousel.js',
    'forrester-successmap.js',
    'forrester-searchresults.js',
    'forrester-analyst.js',
    'forrester-googlemap.js',
    'forrester-stream.js',
    'forrester-toolbar.js',
    'fonts-min.css',
    'modules.css',
    'hub-results-style.css',
    'overlay.css',
    'union.css',
    'forrester-styles.css',
    'jqtransform.css',
    'role-hp.css',
    'header.css',
    'print.css'
]


# This method will add the version in the filename
def update_filename(p_filename):
    string_length = len(p_filename)
    index_of_ext = filename.rfind('.', 0, string_length)
    return filename[0:index_of_ext] + "_" + version + filename[index_of_ext:]


# Iterates through the directories and update each file that exist in the files_to_update list
for directory in directories:
    for filename in os.listdir(directory):
        if filename in files_to_update:
            print("filename: " + directory + filename)
            updated_filename = update_filename(filename)
            print("new filename: " + directory + updated_filename)
            # Updates the filesystem
            os.rename(directory + filename, directory + updated_filename)
