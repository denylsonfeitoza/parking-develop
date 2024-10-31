from django.urls import path
from .views import (
    ParkingList,
    ParkingDetail,
    ParkingSpaceList,
    ParkingSpaceDetail,
    PCDParkingSpaceList,
    TicketList,
    TicketDetail,
    SubscriptionPlanList,
    SubscriptionPlanDetail,
    SubscriberAvailableParkingsList,
    SubscriberListCreateView,
    CarListCreateView,
    CarDetailView,
)

urlpatterns = [
    path('parkings/', ParkingList.as_view(), name='parking-list'),
    path('parkings/<int:pk>/', ParkingDetail.as_view(), name='parking-detail'),
    path('parking-spaces/', ParkingSpaceList.as_view(), name='parking-space-list'),
    path('parking-spaces/<int:pk>/', ParkingSpaceDetail.as_view(), name='parking-space-detail'),
    path('tickets/', TicketList.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='ticket-detail'),
    path('subscription-plans/', SubscriptionPlanList.as_view(), name='subscription-plan-list'),
    path('subscription-plans/<int:pk>/', SubscriptionPlanDetail.as_view(), name='subscription-plan-detail'),
    path('subscriber/available-parkings/', SubscriberAvailableParkingsList.as_view(), name='subscriber-available-parkings'),
    path('subscribers/', SubscriberListCreateView.as_view(), name='subscriber-list-create'),
    path('parking-spaces/pcd/', PCDParkingSpaceList.as_view(), name='pcd-parking-space-list'),
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
]
