import grpc
import service_pb2
import service_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = service_pb2_grpc.RecommenderStub(channel)
    response = stub.GetRecommendation(service_pb2.Request(depart="Casablanca", arrivee="Rabat"))
    print(f"Prix: {response.prix}, Durée: {response.duree}, Transport: {response.moyen_transport}")

if __name__ == '__main__':
    run()
