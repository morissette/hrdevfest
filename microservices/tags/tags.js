'use strict';

const Hapi = require('hapi');
const Boom = require('boom');

/*
 * Setup Server
 */
var server = new Hapi.Server();
server.connection({port: 5001});

/*
 * Setup Routes
 */
server.route({
  method: ['GET', 'POST', 'PUT', 'DELETE'],
  path: '/v1/tag/{tag_uuid?}',
  handler: function(request, reply) {
    /*
     * Request logging
     */
    var timestamp = new Date(request.info.received);
    console.log(`${timestamp} - ${request.info.remoteAddress} - ${request.method.toUpperCase()} ${request.info.host}${request.path}`);

    /*
     * Handle each method
     * with mock responses
     */
    switch ( request.method ) {

      /*
       * GET Handling
       */
      case 'get':
        if ( request.params.tag_uuid ) {
          return reply({
            "tag_uuid": request.params.tag_uuid,
            "name": "Sample",
            "id": 1,
            "type": 1
          })
        }
        return reply([
            {
              "tag_uuid": "1234-5667-1234-1234",
              "name": "Test",
              "id": 2,
              "type": 1
            },
            {
              "tag_uuid": "4321-1234-4321-1234",
              "name": "Javascript",
              "id": 3,
              "type": 1
            }
        ]);
        break;

      /*
       * POST Handling
       */
      case 'post':
        if ( request.params.tag_uuid ) {
          return reply(Boom.badRequest('Unsupported method'));
        }
        return reply(true);
        break;

      /*
       * PUT Handling
       */
      case 'put':
        if ( request.params.tag_uuid ) {
          return reply(true);
        }
        return reply(Boom.badRequest('Unsupported method'));
        break;

      /*
       * DELETE Handling
       */
      case 'delete':
        if ( request.params.tag_uuid ) {
          return reply(true);
        }
        return reply(Boom.badRequest('Unsupported method'));
        break;
    }
  }
});

/*
 * Start Server
 */
server.start(() => {
  console.log(`started at ${server.info.uri}`);
});

/*
 * Shutdown Server
 */
function shutdown() {
  server.stop(() => console.log('shutdown complete'));
}

process
.once('SIGINT', shutdown)
.once('SIGTERM', shutdown);
