import React from "react";
import Navigation from "./presentationals/Navigation";
import "bulma/css/bulma.css";
import "./style.css";

export default class DefaultLayout extends React.Component {
  render() {
    return (
      <div className="default-layout">
        {/*
        <Head>
          <meta
            name="viewport"
            content="initial-scale=1.0, width=device-width"
          />
          <link
            rel="icon"
            type="image/png"
            href="/static/images/logobeta.png"
          />
        </Head>
        */}
        <Navigation />
        {this.props.children}
      </div>
    );
  }
}
