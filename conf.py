import sys
import os
import time
import sphinx_rtd_theme

html_logo = "images/zammad_logo_70x61.png"
html_favicon = "images/favicon.ico"
project = u'Zammad (for Users)'
copyright = u'%s, The Zammad Foundation' % time.strftime("%Y")
author = u'The Zammad Foundation'

source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build', 'html', 'doctrees']
extensions = [
   'versionwarning.extension',
   'sphinx_tabs.tabs',
   'sphinx.ext.extlinks',
]

locale_dirs = ['locale/']
gettext_compact = "user-docs"
language = "en"

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

html_css_files = [
   'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
   'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
   'theme/theme_overrides.css'
]

# Suppress "WARNING: unknown mimetype for ..." during EPUB builds.
#   https://github.com/sphinx-doc/sphinx/issues/3214
suppress_warnings = ['epub.unknown_project_files']

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:

   # We're running outside of readthedocs and expect the compiled version to match the Git branch.
   git_branch = os.environ.get('ZAMMAD_DOCS_GIT_BRANCH', None)

   if git_branch == 'main':
      branch = 'latest'
   else:
      branch = 'pre-release'

else:

   # Get current version we're on for possible version warning
   rtd_version = os.environ.get('READTHEDOCS_VERSION')

   # If we're **not on latest**, we'll display a deprecation warning.
   if rtd_version == 'latest':
      branch = rtd_version

      # Inject the language switcher script.
      html_js_files = ['theme/language_switcher.js']
   elif rtd_version == 'pre-release':
      branch = "pre-release"
   else:
      branch = "old-version"

# Ensure `version` config is set due to EPUB requirements:
#   WARNING: conf value "version" should not be empty for EPUB3
version = branch

# Default definitions for this documentations version warnings if applicable
# https://sphinx-version-warning.readthedocs.io/en/latest/configuration.html
versionwarning_project_slug = "zammad-admin-documentation"
versionwarning_admonition_type = "warning"
versionwarning_project_version = branch
versionwarning_body_selector = "div.document"

versionwarning_messages = {
   "pre-release": (
      "You're viewing a <strong>pre-release</strong> version of this "
      "documentation! If you want to see the stable, current version of "
      "this documentation, please see "
      '<a href="https://user-docs.zammad.org/en/latest/" '
      'title="current documentation version">here</a>.'
   ),
   "old-version": (
      "You're viewing a <strong>deprecated</strong> version of Zammad's "
      "documentation. If you're still running that version, please consider "
      '<a href="https://docs.zammad.org/en/latest/install/update.html" '
      'title="Updating Zammad">Updating Zammad</a> asap.'
      "If you're a hosted user, please contact support."
   ),
}

# Provide aliases to common external documentation targets.
#   It supports automatic substitution for the current language
#   and branch placeholders.
#
#   :admin-docs:`the administrator documentation <manage/users/index.html>`
#
#   which renders the following link in English docs on pre-release branch:
#
#   https://admin-docs.zammad.org/en/pre-release/manage/users/index.html
#
extlinks = {
   'admin-docs': (f'https://admin-docs.zammad.org/{language}/{branch}/%s', '')
}
