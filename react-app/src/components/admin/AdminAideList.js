import React from "react";
import PropTypes from "prop-types";
import { NavLink } from "react-router-dom";
import { compose } from "react-apollo";
import withUser from "../decorators/withUser";
import withEnums from "../decorators/withEnums";
import RaisedButton from "material-ui/RaisedButton";
import moment from "moment";
import ButtonSubmitWithLoader from "../ui/bulma/ButtonSubmitWithLoader";

const styles = {
  button: {
    width: "120px"
  }
};

class AdminAideList extends React.Component {
  static propTypes = {
    onDeleteClick: PropTypes.func
  };
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    const { getEnumValueFromId } = this.props;
    return (
      <div className="AideList">
        <table className="table">
          <thead>
            <tr>
              <th>Nom</th>
              <th>Auteur</th>
              <th>Mis à jour</th>
              <th>type</th>
              <th>Périmètre d'application</th>
              <th>Statut</th>
              <th>Structure porteuse</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {this.props.aides.edges.map(aide => {
              return (
                <tr key={aide.node.id}>
                  <td>{aide.node.nom}</td>
                  <td>{aide.node.auteur && aide.node.auteur.name}</td>
                  <td>{moment(aide.node.updatedAt).format("LLLL")}</td>
                  <td>{getEnumValueFromId("type", aide.node.type).label}</td>
                  <td>
                    {
                      getEnumValueFromId(
                        "perimetreApplicationType",
                        aide.node.perimetreApplicationType
                      ).label
                    }
                  </td>
                  <td>
                    {
                      getEnumValueFromId(
                        "statusPublication",
                        aide.node.statusPublication
                      ).label
                    }
                  </td>
                  <td>{aide.node.structurePorteuse}</td>
                  <td>
                    {aide.meta.userUiPermissions.includes("edit_aide") && (
                      <NavLink to={`/admin/aide/${aide.node.id}/edit`}>
                        <RaisedButton
                          style={styles.button}
                          label="Editer"
                          primary={true}
                        />
                      </NavLink>
                    )}
                    {aide.meta.userUiPermissions.includes("clone_aide") && (
                      <NavLink
                        to={{
                          pathname: "/admin/aide/create",
                          state: { aide: aide.node }
                        }}
                      >
                        <RaisedButton style={styles.button} label="Cloner" />
                      </NavLink>
                    )}
                    <br />
                    {aide.meta.userUiPermissions.includes("delete_aide") && (
                      <span onClick={e => this.props.onDeleteClick(aide)}>
                        <RaisedButton
                          style={styles.button}
                          label="Supprimer"
                          secondary={true}
                        />
                      </span>
                    )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    );
  }
}

export default compose(
  withUser({ mandatory: true }),
  withEnums()
)(AdminAideList);
