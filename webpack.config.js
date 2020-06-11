module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /nodde_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
};
