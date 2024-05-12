from django.urls import path
from esgmanager import views

urlpatterns = [path('pillars/', views.ListViewPillars.as_view(), name='pillars'),
               path('pillar/<uuid:pk>/', views.DetailViewPillars.as_view(), name='pillar'),
               path('create-pillar/', views.CreateViewPillars.as_view(), name='create_pillar'),
               path('update-pillar/<uuid:pk>/', views.UpdateViewPillars.as_view(), name='update_pillar'),
               path('delete-pillar/<uuid:pk>/', views.DeleteViewPillars.as_view(), name='delete_pillar'),

               path('action-plans/', views.ListViewActionPlan.as_view(), name='action_plans'),
               path('action-plan/<uuid:pk>/', views.DetailViewActionPlan.as_view(), name='action_plan'),
               path('create-action-plan/', views.CreateViewActionPlan.as_view(), name='create_action_plan'),
               path('update-action-plan/<uuid:pk>/', views.UpdateViewActionPlan.as_view(), name='update_action_plan'),
               path('delete-action-plan/<uuid:pk>/', views.DeleteViewActionPlan.as_view(), name='delete_action_plan'),

               path('objectives/', views.ListViewObjectives.as_view(), name='objectives'),
               path('objective/<uuid:pk>/', views.DetailViewObjectives.as_view(), name='objective'),
               path('create-objective/', views.CreateViewObjectives.as_view(), name='create_objective'),
               path('update-objective/<uuid:pk>/', views.UpdateViewObjectives.as_view(), name='update_objective'),
               path('delete-objective/<uuid:pk>/', views.DeleteViewObjectives.as_view(), name='delete_objective'),

               path('actions/', views.ListViewActions.as_view(), name='actions'),
               path('action/<uuid:pk>/', views.DetailViewActions.as_view(), name='action'),
               path('create-action/', views.CreateViewActions.as_view(), name='create_action'),
               path('update-action/<uuid:pk>/', views.UpdateViewActions.as_view(), name='update_action'),
               path('delete-action/<uuid:pk>/', views.DeleteViewActions.as_view(), name='delete_action'),

               path('esg-nav-form-pillar', views.NavFormPillars.as_view(), name='esg_nav_form_pillar'),
               path('esg-nav-form-action-plan', views.NavFormActionPlan.as_view(), name='esg_nav_forms_action_plan'),
               path('esg-nav-form-objectives', views.NavFormObjectives.as_view(), name='esg_nav_forms_objectives'),
               path('esg-nav-form-actions', views.NavFormActions.as_view(), name='esg_nav_forms_actions'),
               path('esg-nav-form-risks', views.NavFormsRisks.as_view(), name='esg_nav_forms_risks'),

               path('env-risks/', views.EnvRiskListView.as_view(), name='env_risks'),
               path('env-risk/<uuid:pk>/', views.EnvRiskDetailView.as_view(), name='env_risk'),
               path('create-env-risk/', views.EnvRiskCreateView.as_view(), name='create_env_risk'),
               path('update-env-risk/<uuid:pk>/', views.EnvRiskUpdateView.as_view(), name='update_env_risk'),
               path('delete-env-risk/<uuid:pk>/', views.EnvRiskDeleteView.as_view(), name='delete_env_risk'),

               path('soc-risks/', views.SocialRiskListView.as_view(), name='soc_risks'),
               path('soc-risk/<uuid:pk>/', views.SocialRiskDetailView.as_view(), name='soc_risk'),
               path('create-soc-risk/', views.SocialRiskCreateView.as_view(), name='create_soc_risk'),
               path('update-soc-risk/<uuid:pk>/', views.SocialRiskUpdateView.as_view(), name='update_soc_risk'),
               path('delete-soc-risk/<uuid:pk>/', views.SocialRiskDeleteView.as_view(), name='delete_soc_risk'),

               path('gov-risks/', views.GovernanceRiskListView.as_view(), name='gov_risks'),
               path('gov-risk/<uuid:pk>/', views.GovernanceRiskDetailView.as_view(), name='gov_risk'),
               path('create-gov-risk/', views.GovernanceRiskCreateView.as_view(), name='create_gov_risk'),
               path('update-gov-risk/<uuid:pk>/', views.GovernanceRiskUpdateView.as_view(), name='update_gov_risk'),
               path('delete-gov-risk/<uuid:pk>/', views.GovernanceRiskDeleteView.as_view(), name='delete_gov_risk'),

               path('cc-risks/', views.ClimateRiskListView.as_view(), name='cc_risks'),
               path('cc-risk/<uuid:pk>/', views.ClimateRiskDetailView.as_view(), name='cc_risk'),
               path('create-cc-risk/', views.ClimateRiskCreateView.as_view(), name='create_cc_risk'),
               path('update-cc-risk/<uuid:pk>/', views.ClimateRiskUpdateView.as_view(), name='update_cc_risk'),
               path('delete-cc-risk/<uuid:pk>/', views.ClimateRiskDeleteView.as_view(), name='delete_cc_risk'),

               ]
