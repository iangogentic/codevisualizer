# Development Workflow Guide
## How to Work with CodeMapper Project

**Last Updated:** September 30, 2025

---

## 🎯 Quick Start

### For AI Agents (Cursor):
The `.cursorrules` file contains complete instructions. You will automatically:
- Check `TASKS.md` before every response
- Reference `PRD.md` for specifications
- Update task status as you work
- Follow acceptance criteria

### For Human Developers:
1. Read `PRD.md` to understand the product
2. Check `TASKS.md` to see what needs to be done
3. Pick a task (respect dependencies)
4. Implement following PRD specifications
5. Update `TASKS.md` when done

---

## 📋 The System

### Core Documents

```
📄 PRD.md (2,138 lines)
   ├─ Complete product specification
   ├─ All features detailed
   ├─ API contracts
   ├─ Database schemas
   ├─ UI/UX specifications
   └─ Success criteria

📋 TASKS.md (3,000+ lines)
   ├─ All tasks broken down
   ├─ Status tracking (TODO → IN PROGRESS → DONE)
   ├─ Dependencies mapped
   ├─ Acceptance criteria
   └─ Week-by-week organization

⚙️ .cursorrules
   ├─ Rules for AI agent
   ├─ Workflow automation
   ├─ Quality standards
   └─ Task management process
```

---

## 🔄 Development Workflow

### Step 1: Check Current Status

```bash
# What are we working on?
# Open TASKS.md and find:
- Tasks with status 🔄 IN PROGRESS
- Next task with status ⬜ TODO (check dependencies)
```

### Step 2: Read Specifications

```bash
# What are the requirements?
# In TASKS.md, find:
- **PRD Reference:** PRD.md p.XX
# Open PRD.md to that page and read specifications
```

### Step 3: Update Task Status

```markdown
# In TASKS.md, change:
**Status:** ⬜ TODO
# To:
**Status:** 🔄 IN PROGRESS
**Assignee:** [Your Name]
**Started:** [Date]
```

### Step 4: Implement

```bash
# Follow this order:
1. Read PRD specifications
2. Write code following specs exactly
3. Write tests (unit + integration)
4. Run tests and verify they pass
5. Check off subtasks in TASKS.md
6. Verify acceptance criteria
```

### Step 5: Complete Task

```markdown
# In TASKS.md, change:
**Status:** 🔄 IN PROGRESS
# To:
**Status:** ✅ DONE
**Completed:** [Date]
**Notes:** [Any important notes or deviations]

# Check off all subtasks:
- [x] All subtasks completed
```

### Step 6: Move to Next Task

```bash
# Find next task:
1. Check dependencies (don't start blocked tasks)
2. Follow critical path when possible
3. Update next task to IN PROGRESS
```

---

## 🎨 Example: Implementing a Task

### User Request:
> "Implement the GitHub URL validation"

### AI Response Process:

**1. Check TASKS.md**
```
Found: TASK-201: GitHub URL Validation
Status: ⬜ TODO
Priority: P0
Dependencies: TASK-105 (complete ✓)
```

**2. Read PRD**
```
PRD Reference: PRD.md p.23, F1.0
Requirements:
- Accept format: https://github.com/{org}/{repo}
- Support SSH format
- Extract org and repo name
- Handle edge cases
```

**3. Update Status**
```markdown
**Status:** 🔄 IN PROGRESS
**Assignee:** AI Agent
**Started:** September 30, 2025
```

**4. Implement**
```python
# Create github/validators.py
def validate_github_url(url: str) -> tuple[str, str]:
    """
    Validate GitHub URL and extract org/repo.
    
    PRD Reference: PRD.md p.23
    
    Args:
        url: GitHub URL (HTTPS or SSH)
        
    Returns:
        tuple: (org, repo)
        
    Raises:
        ValueError: If URL is invalid
    """
    # Implementation following PRD specs...
    pass

# Write tests
def test_validate_github_url_https():
    org, repo = validate_github_url("https://github.com/facebook/react")
    assert org == "facebook"
    assert repo == "react"

# ... more tests
```

**5. Check Off Subtasks**
```markdown
- [x] TASK-201.1: Create github/validators.py
- [x] TASK-201.2: Implement validation function
- [x] TASK-201.3: Write unit tests (10+ cases)
- [x] TASK-201.4: Handle edge cases
```

**6. Verify Acceptance Criteria**
```markdown
✓ Validates correct URLs
✓ Rejects invalid URLs with clear error messages
✓ Test coverage >90%
```

**7. Mark Complete**
```markdown
**Status:** ✅ DONE
**Completed:** September 30, 2025
**Notes:** All acceptance criteria met. Tests passing at 95% coverage.
```

**8. Identify Next Task**
```
Next: TASK-202 (Repository Cloning Service)
Dependencies met ✓
Ready to start
```

---

## 📊 Task Status Legend

### Status Indicators

| Icon | Status | Meaning |
|------|--------|---------|
| ⬜ | TODO | Not started, ready to work on |
| 🔄 | IN PROGRESS | Currently being worked on |
| ✅ | DONE | Complete, all criteria met |
| ⏸️ | BLOCKED | Waiting on dependency |
| 🔍 | REVIEW | Needs code review |
| ❌ | CANCELLED | No longer needed |

### How to Use

```markdown
# Starting work:
**Status:** ⬜ TODO → 🔄 IN PROGRESS

# Finishing work:
**Status:** 🔄 IN PROGRESS → ✅ DONE

# Hit a blocker:
**Status:** 🔄 IN PROGRESS → ⏸️ BLOCKED
**Blocker:** Waiting for TASK-XXX to complete

# Ready for review:
**Status:** 🔄 IN PROGRESS → 🔍 REVIEW
```

---

## 🎯 Critical Path

Follow these tasks in order for fastest progress:

```
Week 0:  TASK-000 (Validation)
         ↓
Week 1:  TASK-101 → 102 → 103 → 104 → 105
         ↓
Week 2:  TASK-201 → 202 → 203 → 204 → 205
         ↓
Week 3:  TASK-301 → 302 → 303 → 304
         ↓
Week 4:  TASK-401 → 402 → 403 → 404 → 405 → 406
         ↓
Week 5:  TASK-501 → 502 → 503 → 504 → 505
         ↓
Week 6:  TASK-601 → 602 → 603 → 604 → 605
         ↓
Week 7:  TASK-701 → 702 → 703 (→ 704 optional)
         ↓
Week 8:  TASK-801 → 802 → 803 → 804
         ↓
Week 9:  TASK-901 → 902 → 903
         ↓
Week 10: TASK-1001 → 1002 → 1003 → 1004
         ↓
         🚀 LAUNCH!
```

---

## 🔍 Finding Information

### "What are the API specifications?"
→ Check `PRD.md` p.44-46

### "What's the database schema?"
→ Check `PRD.md` p.42

### "How should I calculate health scores?"
→ Check `PRD.md` p.47 (algorithm)

### "What colors should I use?"
→ Check `PRD.md` p.54-55 (design system)

### "What's the current progress?"
→ Check `TASKS.md` (count ✅ vs ⬜)

### "What should I work on next?"
→ Check `TASKS.md` (find next ⬜ TODO with dependencies met)

---

## 🧪 Testing Requirements

### Every Task Must Include Tests

**Unit Tests:**
```python
# Backend
def test_function_name():
    # Arrange
    input_data = ...
    
    # Act
    result = function(input_data)
    
    # Assert
    assert result == expected
```

```typescript
// Frontend
describe('ComponentName', () => {
  it('should render correctly', () => {
    render(<ComponentName />);
    expect(screen.getByText('...')).toBeInTheDocument();
  });
});
```

**Integration Tests:**
```python
# Test full API flow
def test_analyze_endpoint_integration():
    response = client.post('/api/analyze', json={
        'github_url': 'https://github.com/test/repo'
    })
    assert response.status_code == 202
    assert 'analysis_id' in response.json()
```

**Acceptance:**
- All tests must pass
- Coverage >80%
- No skipped tests

---

## 📝 Documentation Requirements

### Code Comments

```python
def complex_function(param: Type) -> ReturnType:
    """
    Brief description of what this does.
    
    Detailed explanation if needed.
    
    Args:
        param: What this parameter is for
        
    Returns:
        What gets returned
        
    Raises:
        ValueError: When this happens
        
    PRD Reference: PRD.md p.XX
    """
    pass
```

### Update Documentation When:
- Adding new setup steps → `DEVELOPMENT.md`
- Changing API → `API.md` (if exists)
- New features → `CHANGELOG.md`
- Architecture changes → Document in code + update PRD if major

---

## 🚨 Common Issues

### Issue: "I don't know which task to work on"
**Solution:**
1. Open `TASKS.md`
2. Find tasks with status ⬜ TODO
3. Check dependencies are complete (✅)
4. Start with lowest number (respects priority)

### Issue: "Task is blocked"
**Solution:**
1. Mark task as ⏸️ BLOCKED in `TASKS.md`
2. Note which dependency is blocking
3. Find alternative task to work on
4. Or work on unblocking the dependency

### Issue: "Specification is unclear"
**Solution:**
1. Check PRD.md thoroughly
2. Check related sections (API contracts, schemas, etc.)
3. If still unclear, note in TASKS.md and ask for clarification
4. Don't implement without clear spec

### Issue: "Task is taking longer than estimated"
**Solution:**
1. Update estimate in `TASKS.md`
2. Note progress so far
3. Identify what's causing delay
4. Continue or ask for help

---

## ✅ Quality Checklist

Before marking task as ✅ DONE:

- [ ] All subtasks checked off
- [ ] Code follows PRD specifications exactly
- [ ] Unit tests written and passing
- [ ] Integration tests written and passing (if applicable)
- [ ] Code coverage >80%
- [ ] Linting passes (no errors)
- [ ] All acceptance criteria met
- [ ] Documentation updated (if needed)
- [ ] TASKS.md status updated
- [ ] Next task identified

---

## 📈 Progress Tracking

### Daily:
```bash
# Count completed tasks
grep "✅ DONE" TASKS.md | wc -l

# Find in-progress tasks
grep "🔄 IN PROGRESS" TASKS.md
```

### Weekly:
```bash
# Calculate percentage complete
# Total MVP tasks: 74
# Completed: [count]
# Percentage: (completed / 74) * 100
```

### Report Format:
```
Week X of 10 - [Phase Name]

Progress: XX/74 tasks (XX%)
- Completed this week: X tasks
- In progress: X tasks
- Blocked: X tasks

On Track: [Yes/No]
Next Milestone: [Name]

Recent completions:
- TASK-XXX: [Description]

Next up:
- TASK-XXX: [Description]
```

---

## 🎓 Best Practices

### DO:
✅ Read PRD before implementing
✅ Update TASKS.md frequently
✅ Write tests first (TDD)
✅ Check off subtasks as you go
✅ Verify acceptance criteria
✅ Document complex code
✅ Ask questions if unclear
✅ Follow coding standards

### DON'T:
❌ Start without checking TASKS.md
❌ Implement without reading PRD
❌ Skip tests
❌ Leave tasks half-done
❌ Ignore acceptance criteria
❌ Change specs without discussion
❌ Work on blocked tasks
❌ Forget to update status

---

## 🔄 AI Agent Behavior

### What the AI Will Do:

**Before Every Response:**
1. Check TASKS.md for current task
2. Read relevant PRD section
3. Understand acceptance criteria

**While Working:**
1. Follow PRD specifications exactly
2. Write tests for all code
3. Check off subtasks in TASKS.md
4. Document complex logic

**After Completing:**
1. Verify acceptance criteria
2. Update TASKS.md to ✅ DONE
3. Identify next task
4. Report progress

### What to Expect:

```
AI: "I'll implement TASK-XXX: [Name]

According to PRD.md p.XX, the specifications are:
- [List specs]

Updating TASKS.md to IN PROGRESS...

[Implements with tests]

✅ Task complete. All acceptance criteria met.
Updated TASKS.md.

Next task: TASK-YYY. Proceed?"
```

---

## 📞 Getting Help

### If Stuck:
1. Check PRD.md for specifications
2. Check RESEARCH_ANALYSIS.md for decisions
3. Check QUICK_START_GUIDE.md for examples
4. Ask specific questions referencing task number

### If Unsure About Requirements:
1. Note the ambiguity
2. Reference the PRD section
3. Propose a reasonable interpretation
4. Ask for confirmation

### If Timeline Concern:
1. Flag early
2. Explain the delay
3. Propose solution (more time, reduce scope, etc.)
4. Update estimates in TASKS.md

---

## 🎯 Success Metrics

**You're doing it right when:**

1. Every task has clear status
2. Progress is visible in TASKS.md
3. All code has tests
4. PRD specifications are followed
5. Acceptance criteria are met
6. Documentation is current
7. Timeline is on track

**Project success = 74 tasks complete in 10 weeks! 🚀**

---

## 🚀 Let's Build!

**Remember:**
- TASKS.md = What to do
- PRD.md = How to do it
- .cursorrules = Workflow automation
- This guide = Reference

**Now start with:**
```
1. Open TASKS.md
2. Find TASK-000 (Weekend Validation)
3. Check PRD reference
4. Update status to IN PROGRESS
5. Begin work!
```

**Good luck building CodeMapper! 🎨**

