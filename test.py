from PubSub import Bus, Subscriber

bus = Bus()

steve = Subscriber('Steve')
dan = Subscriber('Dan')

bus.subscribe('room1', steve)
bus.subscribe('room1', dan)
bus.subscribe('room2', dan)

bus.publish('room1', 'Welcome to chat room 1!')
bus.publish('room2', 'Welcome to chat room 2!')
bus.publish('room3', 'Welcome to chat room 3!')  # no subscribers
