import React from "react";
import PropTypes from "prop-types";
import moment from "moment";
import { getLabelFromEnumId } from "modules/aide/enums";

const styles = {
  table: {
    width: "100%",
    marginTop: "2rem"
  }
};

class AideListItemDetails extends React.Component {
  static propTypes = {
    aide: PropTypes.object.isRequired
  };
  render() {
    const { aide } = this.props;
    return (
      <div className="AideListItemDetails">
        <table className="table" style={styles.table}>
          <tbody>
            <tr>
              <td>Date d'échéance</td>
              <td>
                {!aide.dateEcheance && "Non renseignée"}
                {aide.dateEcheance && moment(aide.dateEcheance).format("LLLL")}
              </td>
            </tr>
            <tr>
              <td>Lien vers le site</td>
              <td>
                <a target="_blank" href={aide.lien}>
                  Lien vers le site
                </a>
              </td>
            </tr>
            {aide.beneficiaires && (
              <tr>
                <td>Bénéficiaires </td>
                <td>
                  {aide.beneficiaires
                    .map(option => getLabelFromEnumId("beneficiaires", option))
                    .join(", ")}
                </td>
              </tr>
            )}
            <tr>
              <td>Porteur du dispositif</td>
              <td>{aide.structurePorteuse}</td>
            </tr>
            <tr>
              <td>Modalité de diffusion</td>
              <td>
                {aide.formeDeDiffusion
                  .map(option => getLabelFromEnumId("formeDeDiffusion", option))
                  .join(", ")}
              </td>
            </tr>
            <tr>
              <td>Périmètre application</td>
              <td>{aide.perimetreApplicationType}</td>
            </tr>
            <tr>
              <td>Type d'aide</td>
              <td>{aide.type}</td>
            </tr>
            <tr>
              <td>Temporalité dans le projet</td>
              <td>
                {aide.etape
                  .map(option => getLabelFromEnumId("etape", option))
                  .join(", ")}
              </td>
            </tr>
            <tr>
              <td>Destination de l'aide</td>
              <td>
                {aide.destination
                  .map(option => getLabelFromEnumId("destination", option))
                  .join(", ")}
              </td>
            </tr>
          </tbody>
        </table>
        <div className="thematiques">
          {aide.thematiques &&
            aide.thematiques.map(thematique => {
              return (
                <div
                  key={thematique}
                  className="tag is-success"
                  style={{ marginRight: "20px" }}
                >
                  {thematique}
                </div>
              );
            })}
        </div>
      </div>
    );
  }
}

export default AideListItemDetails;
