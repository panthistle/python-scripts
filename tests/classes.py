
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


# # TESTS

# print(f'Test class repr: {repr(Test)}')
# print(f'Test class str: {str(Test)}')
# print(f'Test class type: {type(Test)}')
# print(f'Test class id {id(Test)}')
# print('-'*20)

# m = Test('Mary')
# m.get_name()
# print('-'*10)
# # print will use repr()/str() to represent object
# print(f'Mary instance: {m}')
# print(f'Mary instance repr: {repr(m)}')
# print(f'Mary instance str: {str(m)}')
# print(f'Mary instance type: {type(m)}')
# print(f'Mary instance id: {id(m)}')
# print('-'*20)

# g = Test('George')
# g.get_name()
# print('-'*10)
# print(f'George instance: {g}')
# print(f'George instance type: {type(g)}')
# print(f'George instance id: {id(g)}')
# print('-'*20)

# # storing object info with repr()
# rp = repr(m)
# print(f'stored repr: {rp}')
# print(f'stored repr object type: {type(rp)}')
# print('-'*20)


# ------------------------------------------------------------------------------
#
# -------------------------- object relations ----------------------------------

# ONE-TO-MANY RELATIONS EXAMPLE
# - using uuid module for object unique id
# - using dictionary for uid->object associative array

import uuid


class Entity:
    ''' object class - Registry managed '''

    # initialize
    def __init__(self, pid='', name='', val=0):
        self._uid = self._uid_get()     # object ID
        self.pid = pid                  # parent ID
        self.name = name
        self.val = val
        #...

    # public-access
    @property
    def uid(self):
        return self._uid
    # ...

    # private-access intended
    def _uid_get(self):
        # make a UUID based on the host ID and current time
        #uuid.uuid1()

        # make a random UUID
        x = uuid.uuid4()
        return str(x)


class Registry:
    ''' one-to-many relations management class '''

    def __init__(self):
        self._objects = {}      # 'Entity' objects container

    # public-access
    @property
    def entries(self):
        return list(self._objects.keys())

    def clear(self):
        self._objects.clear()

    def object_exists(self, key):
        return (key in self._objects)

    def add_object(self, name, val, pkey=''):
        # add new object, optionally set existing entry as the parent

        if pkey not in self._objects:
            pkey = ''
        ob = Entity(pkey, name, val)
        key = ob.uid    # new unique key
        self._objects[key] = ob
        return key

    def remove_object(self, key):
        # delete object, leave children with object's parent or None

        if self._valid_key(key):
            ob = self._objects[key]
            self._change_parent(key, ob.pid)
            del self._objects[key]

    def set_parent(self, key, pkey, leave_children=False):
        # set parent reference

        if not (self._valid_key(key) and self._valid_key(pkey)):
            return 'invalid reference'
        if pkey == key:
            return 'cannot set self as parent'
        if pkey in self._descendants(key, []):
            return 'cannot set descendant as parent'
        ob = self._objects[key]
        if ob.pid == pkey:
            return 'parent is already set'
        if leave_children:
            # leave children with old parent or None
            self._change_parent(key, ob.pid)
        ob.pid = pkey
        return 'done'

    def remove_parent(self, key, leave_children=False):
        # remove parent reference

        if not self._valid_key(key):
            return
        ob = self._objects[key]
        if not ob.pid:
            return
        if leave_children:
            # leave children with old parent or None
            self._change_parent(key, ob.pid)
        ob.pid = ''

    def change_name(self, key, new_name):
        if self._valid_key(key):
            self._objects[key].name = new_name

    def object_info(self, key):
        if not self._valid_key(key):
            return ''
        ob = self._objects[key]
        info = f'Name: {ob.name}\n'
        if ob.pid:
            info += f'Parent: {self._objects[ob.pid].name}\n'
        else:
            info += 'Parent: None\n'
        lst = self._ancestors(key, [])
        if lst:
            info += 'Ancestors: '
            for aid in lst:
                info += f'{self._objects[aid].name} '
            info += '\n'
        else:
            info += 'Ancestors: None\n'
        lst = self._children(key)
        if lst:
            info += 'Children: '
            for cid in lst:
                info += f'{self._objects[cid].name} '
            info += '\n'
        else:
            info += 'Children: None\n'
        lst = self._descendants(key, [])
        if lst:
            info += 'Descendants: '
            for did in lst:
                info += f'{self._objects[did].name} '
            info += '\n'
        else:
            info += 'Descendants: None\n'
        return info

    def object_value(self, key):
        if not self._valid_key(key):
            return 0
        ob = self._objects[key]
        div = len(self._children(ob.pid))
        inval = self._inherited_val(key) / div if div else 0
        return inval + ob.val

    # private-access intended
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
        lst = [ob.uid for ob in self._objects.values() if ob.pid == key]
        return lst

    def _inherited_val(self, key, val=0):
        pid = self._objects[key].pid
        # if pid in self._objects:    # defensive approach
        # redundant in this implementation
        if pid:
            ob = self._objects[pid]
            # recursion
            val += self._inherited_val(ob.uid, ob.val)
        return val

    def _ancestors(self, key, lst=[]):
        pid = self._objects[key].pid
        # if pid in self._objects:    # defensive approach
        # redundant in this implementation
        if pid:
            lst.append(pid)
            p = self._objects[pid]
            # recursion
            lst = self._ancestors(p.uid, lst)
        return lst

    def _descendants(self, key, lst=[]):
        children = self._children(key)
        for uid in children:
            lst.append(uid)
            # recursion
            lst = self._descendants(uid, lst)
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
rel_d = rdb.add_object('Jim', 2)
rdb.set_parent(rel_d, rel_b)
print(f'added entry name: Jim as child of Jane\n')

# for i in range(2):
#    rdb.add_object(f'Item {i}', i, rel_a)

# for i in range(2, 5):
#    rdb.add_object(f'Item {i}', i, rel_c)
#    rdb.add_object(f'Item {i+5}', i, rel_d)

entries = rdb.entries
for key in entries:
    print(f'entry {key} info:')
    print(f'{rdb.object_info(key)}Value: {rdb.object_value(key)}\n')
print('-'*30)
