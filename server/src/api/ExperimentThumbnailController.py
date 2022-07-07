from flask import Blueprint, jsonify, request, make_response, Response
from src.models.models import ExperimentThumbnail
from src.services import experiment_thumbnail_service
import base64
import logging

ExperimentThumbnailController = Blueprint('ExperimentThumbnailController', __name__)


@ExperimentThumbnailController.route('/get-thumbnail/<experiment_id>', methods=['GET'])
def get_thumbnail(experiment_id):
    data = experiment_thumbnail_service.get_by_experiment_id(ExperimentThumbnail, experiment_id)
    return Response(data['thumbnail'], mimetype="image/png")