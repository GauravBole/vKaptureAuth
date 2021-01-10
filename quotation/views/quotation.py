from flask.views import MethodView
from flask import Blueprint, request,  make_response, jsonify, url_for, redirect
from exceptions.dao_exceptions import DaoExceptionError
from exceptions.exception_error import ExceptionError



class QuotationApiView(MethodView):

    def post(self, *arge, **kwargs):
        response_data = {"message": {'msg': "something wents wrong"}, "status": "fail", "status_code": 501}
        try:
            post_data = request.form.to_dict()
        except (ExceptionError, DaoExceptionError) as e:
            response_data['status_code'] = e.code
            response_data['message'] = e.get_traceback_details()
            # response_data['message'] = e.dict()
        return make_response(jsonify(response_data)), response_data['status_code']
        