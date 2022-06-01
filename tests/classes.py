
# ------------------------------------------------------------------------------
#
# ------------------------- repr str type id -----------------------------------

class Test:

    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     # will override default __repr__
    #     # return type must be string in angled brackets
    #     return f'<{self.name} is an instance of the Test class>'

    def get_name(self):
        print(self.name)


# TESTS

print(f'Test class repr: {repr(Test)}')
print(f'Test class str: {str(Test)}')
print(f'Test class type: {type(Test)}')
print(f'Test class id {id(Test)}')
print('-'*20)

m = Test('Mary')
m.get_name()
print('-'*10)
# print will use repr()/str() to represent object
print(f'Mary instance: {m}')
print(f'Mary instance repr: {repr(m)}')
print(f'Mary instance str: {str(m)}')
print(f'Mary instance type: {type(m)}')
print(f'Mary instance id: {id(m)}')
print('-'*20)

g = Test('George')
g.get_name()
print('-'*10)
print(f'George instance: {g}')
print(f'George instance type: {type(g)}')
print(f'George instance id: {id(g)}')
print('-'*20)

# storing object info with repr()
rp = repr(m)
print(f'stored repr: {rp}')
print(f'stored repr object type: {type(rp)}')
print('-'*20)


# ------------------------------------------------------------------------------
#
# ------------------------ object associations ---------------------------------

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
        # add new object, optionally set existing entry as the parent

        if not self._valid_key(pkey):
            pkey = ''
        ob = Relation(pkey, name, val)
        key = ob.uid
        self._objects[key] = ob
        return key

    def remove_object(self, key):
        # remove object from registry - adopt orphaned children

        if self._valid_key(key):
            ob = self._objects[key]
            self._change_parent(key, ob.pid)
            del self._objects[key]

    def set_parent(self, key, pkey, leave_children=False):
        # set the parent, leave children with old parent or None

        if not (self._valid_key(key) and self._valid_key(pkey)):
            return 'invalid reference'
        if key == pkey:
            return 'cannot set self as parent'
        ob = self._objects[key]
        if pkey in self._descendants(ob):
            return 'cannot set descendant as parent'
        if ob.pid == pkey:
            return 'parent is already set'
        if leave_children:
            self._change_parent(key, ob.pid)
        ob.pid = pkey
        return 'done'

    def remove_parent(self, key, leave_children=False):
        # remove the parent, leave children with old parent or None

        if not self._valid_key(key):
            return
        ob = self._objects[key]
        pid = ob.pid
        if not pid:
            return
        if leave_children:
            self._change_parent(key, pid)
        ob.pid = ''

    def change_name(self, key, new_name):
        if self._valid_key(key):
            self._objects[key].name = new_name

    def object_info(self, key):
        if not self._valid_key(key):
            return ''
        ob = self._objects[key]
        info = f'my name is {ob.name}. '
        if ob.pid:
            info += f'My parent is {self._objects[ob.pid].name}. '
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
        ob = self._objects[key]
        pid = ob.pid
        div = len(self._children(pid))
        inval = self._inherited_val(pid) / div if div else 0
        return inval + ob.val

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

    def _ancestors(self, ob, lst=[]):
        pid = ob.pid
        if pid:
            lst.append(pid)
            n = self._objects[pid]
            # recursion
            lst = self._ancestors(n, lst)
        return lst

    def _descendants(self, ob):
        uid = ob.uid
        alst = self._ancestors(ob) + [uid]
        items = [i for i in self._objects.values() if i.uid not in alst]
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


# TESTS

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
print(f'entry {rel_a} info:')
print(f'{rdb.object_info(rel_a)}, value: {rdb.object_value(rel_a)}\n')
print(f'entry {rel_b} info:')
print(f'{rdb.object_info(rel_b)}, value: {rdb.object_value(rel_b)}\n')
print(f'entry {rel_c} info:')
print(f'{rdb.object_info(rel_c)}, value: {rdb.object_value(rel_c)}\n')
print(f'entry {rel_d} info:')
print(f'{rdb.object_info(rel_d)}, value: {rdb.object_value(rel_d)}\n')
print(f'try to make Ruth the parent of Harry: {rdb.set_parent(rel_a, rel_c)}')
print('-'*30)

