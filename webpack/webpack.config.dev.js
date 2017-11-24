const path = require('path');
const webpack = require('webpack');

var parentDir = path.join(__dirname, '../');

module.exports = {
    entry: [
        path.join(parentDir, 'index.js')
    ],
    module: {
        loaders: [{
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
            query: {
              presets: ['es2015', 'react']
            },
            test: /\.(css)$/,
            loader: "style-loader!css-loader"
        }]
    },
    output: {
        path: parentDir + '/dist',
        filename: 'bundle.js'
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
    ],
    devServer: {
        contentBase: parentDir,
        historyApiFallback: true
    }
}