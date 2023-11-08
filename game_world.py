objects = [[] for _ in range(4)]


# fill here

def add_object(o, depth=0):
    objects[depth].append(o)


def add_objects(ol, depth=0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


# fill here
# 충돌 그룹 정보를 dictionary 로 표현

collision_pairs = {}  # {boy:ball : [[boy],[ball1, ball2, ... ]]}


def add_collision_pair(group, a, b):  # add_collison_pair('boy:ball', None, ball)
    if group not in collision_pairs:  # dictionary 에 키 group이 없으면
        print(f"new group {group} added.......")
        collision_pairs[group] = [[], []]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()


# fill here
def collide(a, b):
    al, ab, ar, at = a.get_bb()
    bl, bb, br, bt = b.get_bb()
    if al > br:
        return False
    if ab > bt:
        return False
    if at < bb:
        return False
    if ar < bl:
        return False
    return True


def handle_collisons():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
