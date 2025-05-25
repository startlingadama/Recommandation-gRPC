import grpc
from concurrent import futures
import service_pb2
import service_pb2_grpc

class RecommenderServicer(service_pb2_grpc.RecommenderServicer):
    def GetRecommendation(self, request, context):
        print(f"Requête reçue : départ={request.depart}, arrivée={request.arrivee}")
        # Exemple réponse fixe
        return service_pb2.Response(
            prix="150 MAD",
            duree="4h10",
            moyen_transport="Bus"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_RecommenderServicer_to_server(RecommenderServicer(), server)
    server.add_insecure_port('[::]:50051')  # écoute port 50051
    server.start()
    print("Serveur gRPC démarré sur le port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
