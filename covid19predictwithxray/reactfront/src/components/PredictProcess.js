import React, { Component, Fragment } from "react";
import clsx from "clsx";
import { compose } from "redux";
// import { connect } from "react-redux";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import CircularProgress from "@material-ui/core/CircularProgress";
import Typography from "@material-ui/core/Typography";
// import { predictScore } from "../actions/images";
import Alert from "@material-ui/lab/Alert";

const styles = (theme) => ({});

export class PredictProcess extends Component {
  static propTypes = {
    classes: PropTypes.object.isRequired,
  };
  state = {
    predicted: true,
    score: 0,
  };

  componentDidMount() {
    this.setState({
      score: this.props.values.file.score,
    });
  }

  render() {
    const { predicted, score } = this.state;
    const { classes, theme } = this.props;
    const severity = clsx({
      success: score <= 20,
      warning: score < 50 && score > 20,
      error: score >= 50,
    });

    return (
      <Fragment>
        {!predicted && (
          <Fragment>
            <CircularProgress color="secondary" />
            <Typography>Processing Your Chest X-ray ...</Typography>
          </Fragment>
        )}

        {predicted && (
          <Fragment>
            <Alert severity={severity}>
              The chance of being affected by COVID-19 is{" "}
              {(Math.round(score * 100) / 100).toFixed(2)}
              <br />
              {score >= 50 && "Please refer to a doctor as soon as possible"}
            </Alert>
          </Fragment>
        )}
      </Fragment>
    );
  }
}

export default compose(
  withStyles(styles, { withTheme: true })
  // connect(mapStateToProps, { predictScore })
)(PredictProcess);
