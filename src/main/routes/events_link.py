from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.controllers.events_link.events_link_creator import EventsLinkCreator
from src.model.repositories.events_link_repository import EventsLinkRepository

events_link_route_bp = Blueprint("events_link_route", __name__)

@events_link_route_bp.route("/events_link", methods=["POST"])
def create_new_link():
  eventos_link_repo = EventsLinkRepository()
  events_link_creator = EventsLinkCreator(eventos_link_repo)

  http_request = HttpRequest(body=request.json)

  http_response = events_link_creator.create(http_request)

  return jsonify(http_response.body), http_response.status_code