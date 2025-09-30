/**
 * Hierarchical graph layout by folder structure
 * 
 * Organizes nodes by their folder hierarchy for better UX
 */

import { Node, Edge } from 'reactflow';

interface FolderNode {
  path: string;
  children: FolderNode[];
  files: Node[];
  level: number;
}

/**
 * Build folder tree from file paths
 */
function buildFolderTree(nodes: Node[]): FolderNode {
  const root: FolderNode = {
    path: '',
    children: [],
    files: [],
    level: 0
  };

  nodes.forEach(node => {
    const path = node.data.path || node.id;
    const parts = path.split(/[/\\]/).filter((p: string) => p);
    
    let current = root;
    let currentPath = '';
    
    // Navigate/create folder structure
    for (let i = 0; i < parts.length - 1; i++) {
      currentPath += (currentPath ? '/' : '') + parts[i];
      
      const folderPath = currentPath;  // Capture for closure
      let folder = current.children.find(c => c.path === folderPath);
      if (!folder) {
        folder = {
          path: folderPath,
          children: [],
          files: [],
          level: i + 1
        };
        current.children.push(folder);
      }
      current = folder;
    }
    
    // Add file to its folder
    current.files.push(node);
  });

  return root;
}

/**
 * Calculate positions for hierarchical layout
 */
function layoutFolder(folder: FolderNode, startX: number, startY: number): { nodes: Node[], nextY: number } {
  const FOLDER_INDENT = 250;
  const FILE_SPACING_Y = 100;
  const FILE_SPACING_X = 300;
  
  let currentY = startY;
  const layoutedNodes: Node[] = [];

  // Sort folders and files
  folder.children.sort((a, b) => a.path.localeCompare(b.path));
  folder.files.sort((a, b) => (a.data.label || '').localeCompare(b.data.label || ''));

  // Layout files in this folder first (in rows)
  folder.files.forEach((file, idx) => {
    const row = Math.floor(idx / 3);  // 3 files per row
    const col = idx % 3;
    
    layoutedNodes.push({
      ...file,
      position: {
        x: startX + (col * FILE_SPACING_X),
        y: currentY + (row * FILE_SPACING_Y)
      }
    });
  });

  if (folder.files.length > 0) {
    currentY += Math.ceil(folder.files.length / 3) * FILE_SPACING_Y + 50;
  }

  // Layout subfolders recursively
  folder.children.forEach(subfolder => {
    const result = layoutFolder(
      subfolder,
      startX + FOLDER_INDENT,
      currentY
    );
    layoutedNodes.push(...result.nodes);
    currentY = result.nextY + 100;  // Spacing between folders
  });

  return { nodes: layoutedNodes, nextY: currentY };
}

/**
 * Apply hierarchical layout to graph
 */
export function applyHierarchicalLayout(nodes: Node[], edges: Edge[]): { nodes: Node[], edges: Edge[] } {
  if (nodes.length === 0) return { nodes, edges };

  // Build folder tree
  const tree = buildFolderTree(nodes);
  
  // Layout the tree
  const { nodes: layoutedNodes } = layoutFolder(tree, 50, 50);

  return {
    nodes: layoutedNodes,
    edges
  };
}

