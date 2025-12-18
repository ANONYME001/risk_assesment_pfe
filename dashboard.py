"""
Tableau de bord d'évaluation de l'empreinte carbone pour les investissements
Dashboard moderne et professionnel pour l'évaluation des risques carbone
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import sys
from pathlib import Path

# Ajouter le chemin du projet
sys.path.insert(0, str(Path(__file__).parent / "pfe_project" / "src"))

from pfe_project.models import CompanyData, InvestmentAssessment
from pfe_project.calculator import CarbonFootprintCalculator

# Configuration de la page
st.set_page_config(
    page_title="Évaluation Carbone - Investissements",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "### Calculatrice d'Empreinte Carbone\nOutil professionnel d'évaluation des risques carbone pour les investissements"
    }
)

# CSS personnalisé pour un design moderne
st.markdown("""
<style>
    [data-testid="stMetricValue"] {
        font-size: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .header-title {
        color: #1f77b4;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .risk-high {
        color: #d62728;
        font-weight: bold;
    }
    .risk-medium {
        color: #ff7f0e;
        font-weight: bold;
    }
    .risk-low {
        color: #2ca02c;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialiser la session state
if "calculator" not in st.session_state:
    st.session_state.calculator = None
if "assessment_complete" not in st.session_state:
    st.session_state.assessment_complete = False

# ============================================================================
# HEADER
# ============================================================================
st.markdown('<div class="header-title">🌍 Évaluation d\'Empreinte Carbone</div>', unsafe_allow_html=True)
st.markdown("### Outil d'Analyse des Risques Carbone pour Investissements")
st.divider()

# ============================================================================
# SIDEBAR - Informations Entreprise
# ============================================================================
with st.sidebar:
    st.header("📋 Informations Entreprise")
    
    company_name = st.text_input(
        "Nom de l'entreprise",
        value="Nouvelle Entreprise",
        help="Entrez le nom de l'entreprise à évaluer"
    )
    
    annual_revenue = st.number_input(
        "Revenu annuel (en millions $)",
        value=50.0,
        min_value=0.1,
        step=1.0,
        help="Entrez le revenu annuel de l'entreprise"
    )
    
    st.divider()
    st.header("⚙️ Paramètres d'Évaluation")
    
    risk_threshold = st.slider(
        "Seuil de risque carbone",
        min_value=100,
        max_value=5000,
        value=1000,
        step=100,
        help="kg CO2e par million $ de revenu"
    )

# ============================================================================
# MAIN CONTENT - Tabs
# ============================================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Saisie des Données",
    "📈 Résultats",
    "🎯 Évaluation du Risque",
    "📋 Rapport Détaillé"
])

# ============================================================================
# TAB 1 - Saisie des Données
# ============================================================================
with tab1:
    st.header("Saisie des Données d'Émissions")
    
    # Créer la calculatrice
    company = CompanyData(company_name=company_name)
    calculator = CarbonFootprintCalculator(company)
    st.session_state.calculator = calculator
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔥 Portée 1 - Émissions Directes")
        
        with st.expander("Combustibles Fossiles", expanded=True):
            col_f1, col_f2, col_f3 = st.columns(3)
            with col_f1:
                diesel_qty = st.number_input(
                    "Diesel (litres)",
                    value=5000,
                    min_value=0,
                    step=100,
                    key="diesel"
                )
            with col_f2:
                petrol_qty = st.number_input(
                    "Essence (litres)",
                    value=0,
                    min_value=0,
                    step=100,
                    key="petrol"
                )
            with col_f3:
                gas_qty = st.number_input(
                    "Gaz naturel (m³)",
                    value=1000,
                    min_value=0,
                    step=100,
                    key="gas"
                )
            
            # Ajouter les émissions
            if diesel_qty > 0:
                calculator.add_fossil_fuel_emission(
                    "diesel", diesel_qty, 
                    facility_name="Installation principale",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
            if petrol_qty > 0:
                calculator.add_fossil_fuel_emission(
                    "petrol", petrol_qty,
                    facility_name="Installation principale",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
            if gas_qty > 0:
                calculator.add_fossil_fuel_emission(
                    "natural_gas", gas_qty,
                    facility_name="Installation principale",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
        
        with st.expander("Fuite de Réfrigération/Climatisation"):
            refrig_qty = st.number_input(
                "Quantité de réfrigérant (kg)",
                value=0,
                min_value=0,
                step=10,
                key="refrig"
            )
            # TODO: Ajouter méthode add_refrigeration si nécessaire
    
    with col2:
        st.subheader("⚡ Portée 2 - Électricité")
        
        with st.expander("Sources d'Électricité", expanded=True):
            col_e1, col_e2, col_e3 = st.columns(3)
            
            with col_e1:
                grid_qty = st.number_input(
                    "Réseau (kWh)",
                    value=50000,
                    min_value=0,
                    step=1000,
                    key="grid"
                )
            
            with col_e2:
                coal_qty = st.number_input(
                    "Charbon (kWh)",
                    value=10000,
                    min_value=0,
                    step=1000,
                    key="coal"
                )
            
            with col_e3:
                solar_qty = st.number_input(
                    "Solaire (kWh)",
                    value=0,
                    min_value=0,
                    step=1000,
                    key="solar"
                )
            
            # Ajouter les émissions
            if grid_qty > 0:
                calculator.add_electricity_emission(
                    "grid", grid_qty,
                    facility_name="Installation principale",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
            if coal_qty > 0:
                calculator.add_electricity_emission(
                    "coal", coal_qty,
                    facility_name="Installation principale",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
            if solar_qty > 0:
                calculator.add_electricity_emission(
                    "solar", solar_qty,
                    facility_name="Installation principale",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("💧 Portée 3 - Eau et Déchets")
        
        with st.expander("Consommation d'Eau"):
            water_supply = st.number_input(
                "Eau approvisionnée (m³)",
                value=500,
                min_value=0,
                step=50,
                key="water_supply"
            )
            wastewater = st.number_input(
                "Eaux usées (m³)",
                value=300,
                min_value=0,
                step=50,
                key="wastewater"
            )
            
            if water_supply > 0:
                calculator.add_water_emission(
                    "supply", water_supply,
                    facility_name="Installation principale",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
            if wastewater > 0:
                calculator.add_water_emission(
                    "wastewater", wastewater,
                    facility_name="Installation principale",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
        
        with st.expander("Gestion des Déchets"):
            landfill = st.number_input(
                "Décharge (kg)",
                value=1000,
                min_value=0,
                step=100,
                key="landfill"
            )
            recycling = st.number_input(
                "Recyclage (kg)",
                value=500,
                min_value=0,
                step=100,
                key="recycling"
            )
            
            if landfill > 0:
                calculator.add_waste_emission(
                    "landfill", landfill,
                    facility_name="Installation principale",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
            if recycling > 0:
                calculator.add_waste_emission(
                    "recycling", recycling,
                    facility_name="Installation principale",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
    
    with col4:
        st.subheader("✈️ Voyages Professionnels")
        
        with st.expander("Transport"):
            car_km = st.number_input(
                "Automobile (km)",
                value=5000,
                min_value=0,
                step=500,
                key="car"
            )
            air_long = st.number_input(
                "Vol long-courrier (km)",
                value=20000,
                min_value=0,
                step=1000,
                key="air_long"
            )
            rail_km = st.number_input(
                "Train (km)",
                value=0,
                min_value=0,
                step=500,
                key="rail"
            )
            
            if car_km > 0:
                calculator.add_business_travel(
                    "car", car_km,
                    facility_name="Bureau",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
            if air_long > 0:
                calculator.add_business_travel(
                    "air_long", air_long,
                    facility_name="Bureau",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
            if rail_km > 0:
                calculator.add_business_travel(
                    "rail", rail_km,
                    facility_name="Bureau",
                    month=datetime.now().month,
                    year=datetime.now().year
                )
    
    st.divider()
    
    # Bouton de calcul
    if st.button("🧮 Calculer l'Empreinte Carbone", use_container_width=True, type="primary"):
        st.session_state.assessment_complete = True
        st.rerun()

# ============================================================================
# TAB 2 - Résultats
# ============================================================================
with tab2:
    if st.session_state.calculator is not None:
        calculator = st.session_state.calculator
        assessment = InvestmentAssessment(
            company_data=calculator.company_data,
            risk_threshold=risk_threshold
        )
        
        total_emissions = assessment.get_total_emissions()
        scope_breakdown = assessment.get_scope_breakdown()
        
        st.header(f"📊 Résultats pour {company_name}")
        
        # KPIs
        col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
        
        with col_kpi1:
            st.metric(
                "Émissions Totales",
                f"{total_emissions:,.0f}",
                delta="kg CO2e"
            )
        
        with col_kpi2:
            scope1 = scope_breakdown["Portée 1 (Directe)"]
            st.metric(
                "Portée 1",
                f"{scope1:,.0f}",
                delta=f"{scope1/total_emissions*100:.1f}%" if total_emissions > 0 else "0%"
            )
        
        with col_kpi3:
            scope2 = scope_breakdown["Portée 2 (Énergie)"]
            st.metric(
                "Portée 2",
                f"{scope2:,.0f}",
                delta=f"{scope2/total_emissions*100:.1f}%" if total_emissions > 0 else "0%"
            )
        
        with col_kpi4:
            scope3 = scope_breakdown["Portée 3 (Autre)"]
            st.metric(
                "Portée 3",
                f"{scope3:,.0f}",
                delta=f"{scope3/total_emissions*100:.1f}%" if total_emissions > 0 else "0%"
            )
        
        st.divider()
        
        # Graphiques
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.subheader("Répartition par Portée")
            
            # Pie chart
            scope_labels = list(scope_breakdown.keys())
            scope_values = list(scope_breakdown.values())
            
            fig_scope = go.Figure(data=[go.Pie(
                labels=scope_labels,
                values=scope_values,
                hole=0.3,
                marker=dict(colors=['#1f77b4', '#ff7f0e', '#2ca02c'])
            )])
            
            fig_scope.update_layout(
                height=400,
                font=dict(size=12),
                showlegend=True
            )
            
            st.plotly_chart(fig_scope, use_container_width=True)
        
        with col_chart2:
            st.subheader("Répartition par Catégorie")
            
            emissions_by_category = calculator.company_data.get_emissions_by_category()
            
            fig_category = go.Figure(data=[go.Bar(
                x=list(emissions_by_category.keys()),
                y=list(emissions_by_category.values()),
                marker=dict(color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
            )])
            
            fig_category.update_layout(
                title="",
                xaxis_title="Catégorie",
                yaxis_title="Émissions (kg CO2e)",
                height=400,
                showlegend=False,
                hovermode='x unified'
            )
            
            st.plotly_chart(fig_category, use_container_width=True)
    else:
        st.info("👈 Veuillez d'abord saisir les données dans l'onglet 'Saisie des Données'")

# ============================================================================
# TAB 3 - Évaluation du Risque
# ============================================================================
with tab3:
    if st.session_state.calculator is not None:
        calculator = st.session_state.calculator
        assessment = InvestmentAssessment(
            company_data=calculator.company_data,
            risk_threshold=risk_threshold
        )
        
        st.header("🎯 Analyse du Risque Carbone")
        
        carbon_intensity = assessment.get_carbon_intensity(annual_revenue)
        is_high_risk = assessment.is_high_risk(annual_revenue)
        recommendation = assessment.get_investment_recommendation(annual_revenue)
        
        # Affichage de l'intensité carbone
        col_intensity1, col_intensity2 = st.columns(2)
        
        with col_intensity1:
            st.metric(
                "Intensité Carbone",
                f"{carbon_intensity:.2f}",
                delta="kg CO2e / $1M revenu"
            )
        
        with col_intensity2:
            st.metric(
                "Seuil de Risque",
                f"{risk_threshold}",
                delta="kg CO2e / $1M revenu"
            )
        
        st.divider()
        
        # Classification du risque
        st.subheader("Classification du Risque")
        
        if carbon_intensity < 100:
            risk_level = "FAIBLE"
            risk_color = "green"
            risk_icon = "✅"
        elif carbon_intensity < 500:
            risk_level = "MODÉRÉ"
            risk_color = "orange"
            risk_icon = "⚠️"
        else:
            risk_level = "ÉLEVÉ"
            risk_color = "red"
            risk_icon = "❌"
        
        st.markdown(f"""
        <div style="
            background-color: {'#90EE90' if risk_color == 'green' else '#FFD700' if risk_color == 'orange' else '#FFB6C6'};
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        ">
            <h2 style="color: {'#2d5016' if risk_color == 'green' else '#8B4513' if risk_color == 'orange' else '#8B0000'};">
                {risk_icon} RISQUE {risk_level}
            </h2>
            <p style="font-size: 18px; color: {'#2d5016' if risk_color == 'green' else '#8B4513' if risk_color == 'orange' else '#8B0000'};">
                Intensité carbone: {carbon_intensity:.2f} kg CO2e / $1M revenu
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Recommandation d'investissement
        st.subheader("💼 Recommandation d'Investissement")
        
        if "ROUGE" in recommendation:
            st.error(recommendation)
        elif "JAUNE" in recommendation:
            st.warning(recommendation)
        else:
            st.success(recommendation)
        
        st.divider()
        
        # Jauge de risque
        st.subheader("Jauge de Risque")
        
        fig_gauge = go.Figure(go.Indicator(
            domain={"x": [0, 1], "y": [0, 1]},
            value=carbon_intensity,
            title={"text": "kg CO2e / $1M revenu"},
            mode="gauge+number+delta",
            delta={"reference": risk_threshold, "suffix": " par rapport au seuil"},
            gauge={
                "axis": {"range": [0, max(carbon_intensity * 1.2, risk_threshold * 1.5)]},
                "bar": {"color": "darkblue"},
                "steps": [
                    {"range": [0, 100], "color": "#90EE90"},
                    {"range": [100, 500], "color": "#FFD700"},
                    {"range": [500, max(carbon_intensity * 1.2, risk_threshold * 1.5)], "color": "#FFB6C6"}
                ],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "thickness": 0.75,
                    "value": risk_threshold
                }
            }
        ))
        
        fig_gauge.update_layout(height=400)
        st.plotly_chart(fig_gauge, use_container_width=True)
    else:
        st.info("👈 Veuillez d'abord saisir les données dans l'onglet 'Saisie des Données'")

# ============================================================================
# TAB 4 - Rapport Détaillé
# ============================================================================
with tab4:
    if st.session_state.calculator is not None:
        calculator = st.session_state.calculator
        
        st.header("📋 Rapport Détaillé")
        
        # Résumé
        st.subheader("Résumé de l'Évaluation")
        
        summary_col1, summary_col2 = st.columns(2)
        
        with summary_col1:
            st.write(f"**Entreprise:** {company_name}")
            st.write(f"**Revenu annuel:** ${annual_revenue:.2f}M")
            st.write(f"**Date d'évaluation:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        with summary_col2:
            assessment = InvestmentAssessment(
                company_data=calculator.company_data,
                risk_threshold=risk_threshold
            )
            st.write(f"**Nombre d'activités:** {len(calculator.company_data.activities)}")
            st.write(f"**Émissions totales:** {assessment.get_total_emissions():,.0f} kg CO2e")
            st.write(f"**Intensité carbone:** {assessment.get_carbon_intensity(annual_revenue):.2f} kg CO2e / $1M")
        
        st.divider()
        
        # Tableau détaillé
        st.subheader("Détail des Émissions")
        
        df = calculator.get_dataframe_report()
        
        # Formater le DataFrame pour l'affichage
        df_display = df.copy()
        df_display['Quantité'] = df_display['Quantité'].apply(lambda x: f"{x:,.2f}")
        df_display['Facteur d\'émission'] = df_display['Facteur d\'émission'].apply(lambda x: f"{x:.4f}")
        df_display['Émissions (kg CO2e)'] = df_display['Émissions (kg CO2e)'].apply(lambda x: f"{x:,.2f}")
        
        st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        st.divider()
        
        # Options de téléchargement
        st.subheader("⬇️ Télécharger les Données")
        
        col_csv, col_excel = st.columns(2)
        
        with col_csv:
            csv = df.to_csv(index=False)
            st.download_button(
                label="📄 Télécharger en CSV",
                data=csv,
                file_name=f"emissions_{company_name.replace(' ', '_')}.csv",
                mime="text/csv"
            )
        
        with col_excel:
            from io import BytesIO
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
            
            st.download_button(
                label="📊 Télécharger en Excel",
                data=buffer.getvalue(),
                file_name=f"emissions_{company_name.replace(' ', '_')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.info("👈 Veuillez d'abord saisir les données dans l'onglet 'Saisie des Données'")

# ============================================================================
# FOOTER
# ============================================================================
st.divider()
st.markdown("""
<div style="text-align: center; color: gray; font-size: 12px; margin-top: 30px;">
    <p>📊 Calculatrice d'Empreinte Carbone | Basée sur le protocole GHG</p>
    <p>Outil professionnel d'évaluation des risques carbone pour les investissements</p>
    <p>© 2025 - Tous droits réservés</p>
</div>
""", unsafe_allow_html=True)
