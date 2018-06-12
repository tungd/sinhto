exports.files = {
  javascripts: {
    joinTo: 'app.js'
  },

  stylesheets: {
    joinTo: 'app.css'
  }
}

exports.modules = {
  autoRequire: {
    'app.js': ['initialize']
  }
}

exports.plugins = {
  babel: {
    presets: ['env', 'react']
  }
}
