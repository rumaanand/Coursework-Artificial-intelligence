import bindings
import copy
class fact(object):
    def __init__(self, statement, supported_by=[]):
        self.statement = statement
        if not supported_by:
            self.asserted = True
        else:
            self.asserted = False
        self.supported_by = supported_by
        self.facts_supported = []
        self.rules_supported = []
        
class rule(object):
    def __init__(self, rule, supported_by=[]):
        self.LHS = rule[0]
        self.RHS = rule[1]
        if not supported_by:
            self.asserted = True
        else:
            self.asserted = False
        self.supported_by = supported_by
        self.facts_supported = []
        self.rules_supported = []


class kb(object):
    def __init__(self):
        self.facts = []
        self.rules = []
        
    def kb_add_fact(self, fact):
        self.facts.append(fact)
        
    def kb_add_rule(self, rule):
        self.rules.append(rule)
        
    def kb_remove_fact(self, fact):
        for myfact in self.facts:
            if myfact.statement == fact.statement:
                break
        self.facts.remove(myfact)
        
    def kb_remove_rule(self, rule):
        for myrule in self.rules:
            if (myrule.LHS == rule.LHS) and (myrule.RHS == rule.RHS):
                break
        self.rules.remove(myrule)                  
  # This function is used to assert a statement after recognizing whether it is a fact or a rule.
    def kb_assert(self, statement):
        if factq(statement):
            new_fact = fact(statement)
            print 'Asserting fact: ', new_fact.statement
            self.facts.append(new_fact)
            self.kb_infer_fact(new_fact)
        else:
            new_rule = rule(statement)
            print 'Asserting rule: ', new_rule.LHS, '=>', new_rule.RHS
            self.rules.append(new_rule)
            self.kb_infer_rule(new_rule)
 # This function is used to infer a fact and calls either kb_infer_fact recursively or kb_infer_rule depending upon the generation of new fact or new rule.
    def kb_infer_fact(self, curr_fact):
        for curr_rule in self.rules:
            curr_bindings = bindings.match(curr_fact.statement, curr_rule.LHS[0])
            if curr_bindings or curr_fact.statement==curr_rule.LHS[0]:
                if len(curr_rule.LHS) == 1:
                    new_statement = instantiate(curr_rule.RHS, curr_bindings)
                    new_fact = fact(new_statement, [curr_fact, curr_rule])
                    if not self.kb_check_fact(new_fact):
                        self.facts.append(new_fact)
                        print '\tInferred new fact: ', new_fact.statement
                        curr_fact.facts_supported.append(new_fact)
                        curr_rule.facts_supported.append(new_fact)
                        self.kb_infer_fact(new_fact)

                else:
                    new_left = []
                    new_right = instantiate(curr_rule.RHS,curr_bindings)
                    for i in range(1,len(curr_rule.LHS)):
                        new_left.append(instantiate(curr_rule.LHS[i],curr_bindings))
                    new_rule = rule([new_left, new_right], [curr_fact, curr_rule])
                    if not self.kb_check_rule(new_rule):
                        self.rules.append(new_rule)
                        print '\tInferred new rule: ', new_rule.LHS, '=>', new_rule.RHS
                        curr_fact.rules_supported.append(new_rule)
                        curr_rule.rules_supported.append(new_rule)
                        self.kb_infer_rule(new_rule)
                
#  This function is used to infer a rule and calls either infer rule recursively or infer fact depending upon the generation of new fact or new rule.

    def kb_infer_rule(self, curr_rule):
        for curr_fact in self.facts:
            curr_bindings = bindings.match(curr_fact.statement, curr_rule.LHS[0])
            if curr_bindings or curr_fact.statement==curr_rule.LHS[0]:
                if len(curr_rule.LHS) == 1:
                    new_statement = instantiate(curr_rule.RHS, curr_bindings)
                    new_fact = fact(new_statement, [curr_fact, curr_rule])
                    if not self.kb_check_fact(new_fact):
                        self.facts.append(new_fact)
                        print '\tInferred new fact: ', new_fact.statement
                        curr_fact.facts_supported.append(new_fact)
                        curr_rule.facts_supported.append(new_fact)
                        self.kb_infer_fact(new_fact)

                else:
                    new_left = []
                    new_right = instantiate(curr_rule.RHS, curr_bindings)
                    for i in range(1,len(curr_rule.LHS)):
                        new_left.append(instantiate(curr_rule.LHS[i], curr_bindings))
                    new_rule = rule([new_left, new_right], [curr_fact, curr_rule])
                    if not self.kb_check_rule(new_rule):
                        self.rules.append(new_rule)
                        print '\tInferred new rule: ', new_rule.LHS, '=>', new_rule.RHS
                        curr_fact.rules_supported.append(new_rule)
                        curr_rule.rules_supported.append(new_rule)
                        self.kb_infer_rule(new_rule)
                

    def kb_ask(self, query):
        curr_bindings = map(lambda(x): bindings.match(x.statement, query), self.facts)
        if curr_bindings:
            return filter(lambda(x): x, curr_bindings)


    def kb_ask_plus(self, queries):
        bindings_list = []
        #for query in queries:
         #   mybindings = self.ask(query)
          #  bindings_list.append(mybindings)
        return bindings_list

# This method is used to given statements by detemining if its a fact or a rule using BFS approach.
    def kb_retract(self, statement):
        print 'Before Retract - KB: Facts# ', len(self.facts), ' and Rule# ', len(self.rules)
        if factq(statement):
            curr_fact = fact(statement)
            print ''
            print 'Retracting fact: ', curr_fact.statement
            for myfact in self.facts:
                if curr_fact.statement == myfact.statement:
                    statement_list = []
                    statement_list.append(myfact)
                    while statement_list:
                        curr_statement = statement_list.pop()
                        if type(curr_statement) == fact:
                            print 'Removing fact: ', curr_statement.statement
                        else:
                            print 'Removing rule: ', curr_statement.LHS, '=>', curr_statement.RHS
                        for curr_fs in curr_statement.facts_supported:
                            print '\tSupported fact: ', curr_fs.statement
                            statement_list.append(curr_fs)
                        for curr_rs in curr_statement.rules_supported:
                            print '\tSupported rule: ', curr_rs.LHS, '=>', curr_rs.RHS
                            statement_list.append(curr_rs)
                        if type(curr_statement) == fact:
                            self.kb_remove_fact(curr_statement)
                        else:
                            self.kb_remove_rule(curr_statement)
        else:
            curr_rule = rule(statement)
            print ''
            print 'Retracting rule: ', curr_rule.LHS, '=>', curr_rule.RHS
            for myrule in self.rules:
                if (myrule.LHS == curr_rule.LHS) and (myrule.RHS == curr_rule.RHS):
                    statement_list = []
                    statement_list.append(myrule)
                    while statement_list:
                        curr_statement = queue.pop()
                        if type(curr_statement) == fact:
                            print 'Removing fact: ', curr_statement.statement
                        else:
                            print 'Removing rule: ', curr_statement.LHS, '=>', curr_statement.RHS
                        for curr_fs in curr.facts_supported:
                            print '\tSupported fact: ', curr_fs.statement
                            statement_list.append(curr_fs)
                        for curr_rs in curr.rules_supported:
                            print '\tSupported rule: ', curr_rs.LHS, '=>', curr_rs.RHS
                            statement_list.append(curr_fs)
                        if type(curr_statement) == fact:
                            self.kb_remove_fact(curr_statement)
                        else:
                            self.kb_remove_rule(curr_statement)
        print 'After Retract - KB: Facts# ', len(self.facts), ' and Rule# ', len(self.rules)
                
# This method explains the origin of the given query.
    def kb_why(self, query):
        if factq(query):
            curr_fact = fact(query)
            result = []
            for myfact in self.facts:
                if curr_fact.statement == myfact.statement:
                    print ''
                    print 'Explaining fact: ', curr_fact.statement
                    statement_list = []
                    statement_list.append(myfact)
                    while statement_list:
                        curr_statement = statement_list.pop()
                        if type(curr_statement) == fact:
                            print 'Fact: ', curr_statement.statement
                        else:
                            print 'Rule: ', curr_statement.LHS,' => ', curr_statement.RHS
                        for curr_cs in curr_statement.supported_by:
                            if type(curr_cs) == fact:
                                print '\tSupported by fact: ', curr_cs.statement
                            else:
                                print '\tSupported by rule: ', curr_cs.LHS,' => ', curr_cs.RHS
                            statement_list.append(curr_cs)
                        if not curr_statement.supported_by:
                            if (type(curr_statement) == fact) and (curr_statement.statement != curr_fact.statement):
                                result.append(curr_statement.statement)
            return result

        else:
            curr_rule = rule(query)
            result = []
            for myrule in self.rules:
                if (myrule.LHS == curr_rule.LHS) and (myrule.RHS == curr_rule.RHS):
                    print 'Explaining rule: ', curr_rule.LHS, '=>', curr_rule.RHS
                    statement_list = []
                    statement_list.append(myrule)
                    while statement_list:
                        curr_statement = statement_list.pop()
                        if type(curr_statement) == fact:
                            print 'Fact: ', curr_statement.statement
                        else:
                            print 'Rule: ', curr_statement.LHS,' => ', curr_statement.RHS
                        for curr_cs in curr_statement.supported_by:
                            if type(curr_cs) == fact:
                                print '\tSupported by fact: ', curr_cs.statement
                            else:
                                print '\tSupported by rule: ', curr_cs.LHS,' => ', curr_cs.RHS
                            statement_list.append(curr_cs)
                        if not curr_statement.supported_by:
                            if (type(curr_statement) == rule) and ((curr_statement.LHS != curr_rule.LHS) or (curr_statement.RHS != curr_rule.RHS)):
                                result.append([curr_statement.LHS,curr_statement.RHS])       
            return result
    
        
    def kb_check_fact(self, myfact):
        found = False
        for cur in self.facts:
            if cur.statement == myfact.statement:
                found = True
                break         
        return found
    
    def kb_check_rule(self, myrule):
        found = False
        for cur in self.rules:
            if (cur.LHS == myrule.LHS) and (cur.RHS == myrule.RHS):
                found = True
                break
        return found
    
def instantiate(statement, bindings):
    curr_bindings = {}
    if type(bindings) is list:
        for mybinding in bindings:
            for key in mybinding.keys():
                curr_bindings[key] = mybinding[key]
    else:
        curr_bindings = bindings
    new_statement = copy.deepcopy(statement)
    for i in range(len(statement)):
        if statement[i][0] == '?':
            if statement[i] in curr_bindings:
                new_statement[i] = curr_bindings[statement[i]]
    return new_statement 

# Tests to see if an input is a statement (as opposed to a rule)
def factq(element):
    return type(element[0]) is str 

# KB_assert Asserts a statement or a rule to a knowledge base. It invokes different code if it is one or the other.
# New facts and rules can trigger inference
def KB_assert(kb, assertion):
    kb.kb_assert(assertion)
        
# KB_ask queries the knowledge base to check if a statement is true.            
def KB_ask(kb, query):
    if factq(query):
        return kb.kb_ask(query)  

# KB_why shows us the supports for a statement
def KB_why(kb, query):
    kb.kb_why(query)

# KB_retract removes a statement from the knowledge base and then all other facts and rules that 
# it supports
def KB_retract(kb, statement):
    kb.kb_retract(statement)
        

# KB_ask_plus queries the knowledge base to check if a list of statements are true. 
def KB_ask_plus(kb, query):
    return kb.kb_ask_plus(query) 
    