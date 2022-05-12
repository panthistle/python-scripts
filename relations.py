
# ONE-TO-MANY RELATIONS EXAMPLE (using uuid module)
import uuid

class Relation:
    ''' object class '''

    # initialize
    def __init__(self, pid='', name='', val=0):
        self.uid = self._uid_get()
        self.pid = pid
        self.name = name
        self.val = val
        #...


    # public methods
    # ...


    # private methods
    def _uid_get(self):
        # make a UUID based on the host ID and current time
        #uuid.uuid1()

        # make a random UUID
        x = uuid.uuid4()
        return str(x)



class Registry:
    ''' one-to-many relations management class '''

    def __init__(self):
        self._objects = {}      # 'Relation' objects container


    # public methods
    def clear(self):
        self._objects.clear()


    def object_exists(self, key):
        if key in self._objects:
            return True
        return False


    def add_object(self, name, val, pkey=''):
        if not self._valid_key(pkey):
            pkey = ''
        rel = Relation(pkey, name, val)
        key = rel.uid
        self._objects[key] = rel
        return key


    def remove_object(self, key):
        # remove object from registry - adopt orphaned children

        if self._valid_key(key):
            rel = self._objects[key]
            self._change_parent(key, rel.pid)
            del self._objects[key]

    
    def set_parent(self, key, pkey, leave_children=False):
        # assign new parent, optionally leave children with old parent or None

        if not (self._valid_key(key) and self._valid_key(pkey)):
            return 'invalid reference'
        if key == pkey:
            return 'cannot set self as parent'
        rel = self._objects[key]
        if pkey in self._descendants(rel):
            return 'cannot set descendant as parent'
        if rel.pid == pkey:
            return 'parent is already set'
        if leave_children:
            self._change_parent(key, rel.pid)
        rel.pid = pkey
        return 'done'


    def remove_parent(self, key, leave_children=False):
        # remove existing parent, optionally leave children behind

        if not self._valid_key(key):
            return
        rel = self._objects[key]
        pid = rel.pid
        if not pid:
            return
        if leave_children:
            self._change_parent(key, pid)
        rel.pid = ''


    def change_name(self, key, new_name):
        if self._valid_key(key):
            self._objects[key].name = new_name


    def object_info(self, key):
        if not self._valid_key(key):
            return ''
        rel = self._objects[key]
        info = f'my name is {rel.name}. '
        if rel.pid:
            info += f'My parent is {self._objects[rel.pid].name}. '
        else:
            info += 'I have no parent. '
        lst = self._children(key)
        if lst:
            info += 'My children are: '
            for child in lst:
                info += f'{child.name}, '
        else:
            info += 'I have no children.'
        return info


    def object_value(self, key):
        if not self._valid_key(key):
            return 0
        rel = self._objects[key]
        pid = rel.pid
        div = len(self._children(pid))
        inval = self._inherited_val(pid) / div if div else 0
        return inval + rel.val


    # private methods
    def _valid_key(self, key):
        if key in self._objects:
            return True
        print(f'object id - {key} - not found!')
        return False


    def _change_parent(self, old, new):
        for ob in self._objects.values():
            if ob.pid == old:
                ob.pid = new


    def _children(self, key):
        lst = []
        for ob in self._objects.values():
            if ob.pid == key:
                lst.append(ob)
        return lst


    def _inherited_val(self, pid, val=0):
        if pid:
            ob = self._objects[pid]
            # recursion
            val += self._inherited_val(ob.pid, ob.val)
        return val


    def _ancestors(self, rel, lst=[]):
        pid = rel.pid
        if pid:
            lst.append(pid)
            n = self._objects[pid]
            # recursion
            lst = self._ancestors(n, lst)
        return lst


    def _descendants(self, rel):
        uid = rel.uid
        alst = self._ancestors(rel) + [uid]
        items = [item for item in self._objects.values() if item.uid not in alst]
        lst = []
        for item in items:
            if not item.pid:
                continue
            alst = self._ancestors(item)
            for aid in alst:
                if aid == uid:
                    lst.append(item.uid)
                    break
        return lst



rdb = Registry()

print('add/remove parent/child entries')
print('-'*10)
rel_a = rdb.add_object('Harry', 1)
print('added entry name: Harry')
rel_b = rdb.add_object('Jane', 3, rel_a)
print(f'added entry name: Jane as child of Harry')
rel_c = rdb.add_object('Ruth', 5, rel_b)
print(f'added entry name: Ruth as child of Jane')
rel_d = rdb.add_object('Jim', 2, rel_b)
print(f'added entry name: Jim as child of Jane')
print(f'entry {rel_a} info: {rdb.object_info(rel_a)}, value: {rdb.object_value(rel_a)}')
print(f'entry {rel_b} info: {rdb.object_info(rel_b)}, value: {rdb.object_value(rel_b)}')
print(f'entry {rel_c} info: {rdb.object_info(rel_c)}, value: {rdb.object_value(rel_c)}')
print(f'entry {rel_d} info: {rdb.object_info(rel_d)}, value: {rdb.object_value(rel_d)}')
print(f'attempt to make Ruth the parent of Harry: {rdb.set_parent(rel_a, rel_c)}')
print('-'*30)

