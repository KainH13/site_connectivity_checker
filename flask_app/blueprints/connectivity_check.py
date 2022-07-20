from flask import Blueprint, jsonify, request
import asyncio
from http.client import HTTPConnection
from urllib.parse import urlparse
import aiohttp

connectivity_check = Blueprint(name="connectivity_check", import_name=__name__)


@connectivity_check.route("/test", methods=["GET"])
def test():
    output = {"msg": "I'm the test endpoint from connectivity_check."}
    return jsonify(output)


@connectivity_check.route("/basic", methods=["POST"])
def basic_connectivity_check():
    output = {}
    for url in request.json["urls"]:
        output[url] = {}
        error = "unknown error"
        parser = urlparse(url)
        host = parser.netloc or parser.path.split("/")[0]
        for port in (80, 443):  # checks both http and https ports
            connection = HTTPConnection(host=host, port=port, timeout=2)
            try:  # tries to make a head request
                connection.request("HEAD", "/")
                output[url]["status"] = "Online"  # sets status in output dict to Online
            except Exception as e:
                error = str(e)
                # sets status in output dict to Offline and adds error message
                output[url]["status"] = "Offline"
                output[url]["error"] = error
            finally:
                connection.close()
    return output


@connectivity_check.route("/async", methods=["POST"])
async def connectivity_check_async():
    output = {}
    for url in request.json["urls"]:
        output[url] = {}
        error = "unknown error"
        parser = urlparse(url)
        host = parser.netloc or parser.path.split("/")[0]
        for scheme in ("http", "https"):  # check both http and https options
            target_url = scheme + "://" + host
            async with aiohttp.ClientSession() as session:
                try:
                    await session.head(target_url, timeout=2)
                    output[url][
                        "status"
                    ] = "Online"  # sets status in output dict to Online
                except asyncio.exceptions.TimeoutError:
                    error = "timed out"
                    # sets status in output dict to Offline and adds error message
                    output[url]["status"] = "Offline"
                    output[url]["error"] = error
                except Exception as e:
                    error = str(e)
                    output[url]["status"] = "Offline"
                    output[url]["error"] = error
    return output
